import machine
import network
import time
import sys
import neopixel

import WiFi_connect
from umqttsimple import MQTTClient


def hsv_to_rgb(h, s, v):
    if s == 0.0: return (v, v, v)
    i = int(h*6.) # XXX assume int() truncates!
    f = (h*6.)-i; p,q,t = v*(1.-s), v*(1.-s*f), v*(1.-s*(1.-f)); i%=6
    if i == 0: return (v, t, p)
    if i == 1: return (q, v, p)
    if i == 2: return (p, v, t)
    if i == 3: return (p, q, v)
    if i == 4: return (t, p, v)
    if i == 5: return (v, p, q)
 

def ledStrip_setRainbow():
    SEPERATION = 36
    for i in range(leds.n):
        r,g,b = hsv_to_rgb(i/SEPERATION, 1, 1)
        leds[i] = (int(r*255), int(g*255), int(b*255))
    leds.write()

### Process MQTT message
def setLedStrip(mqtt_message):
    hsvData = mqtt_message.split(',')
    print(hsvData)
    h = float(hsvData[0])/float(100)/4.0
    s = float(hsvData[1])/float(100)
    v = float(hsvData[2])/float(100)
    r,g,b = hsv_to_rgb(h, s, v)
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    # r,g,b = hsv_to_rgb(float(hsvData[0])/float(100), 10, .1)
    print("hsv("+ str(h) +","+ str(s) +","+ str(v) +") => rgb("+ str(r) +","+ str(g) +","+ str(b) +")")
    for i in range(leds.n):
        leds[i] = r, g, b
    leds.write()

### MQTT callback
def sub_cb(topic, msg):
    led.off()
    print("MQTT_Rx -> topic: " + topic.decode() + ", message: " + msg.decode())
    if topic == MQTT_TOPIC:
        setLedStrip(msg.decode())
    else:
        print("Unrecognized topic")
    led.on()


###########################################
print('\r\nAppstar....................................1')
print( "\t* System clock: ", machine.freq() / 1000000, "MHz")

### integrated LED
pin_integratedLed = 2
led = machine.Pin(pin_integratedLed, machine.Pin.OUT)
led.off()

### LED Strip
leds_cnt = 60
leds_pin = 4 # D2
leds = neopixel.NeoPixel(machine.Pin(leds_pin), leds_cnt)
ledStrip_setRainbow()

### Connect to WiFi network
wlan = network.WLAN(network.STA_IF)
WiFi_connect.conn1(wlan)

### Connect to MQTT Server
MQTT_TOPIC = b"ledStrip_set"
MQTT_SERVER = "10.0.0.182"
MQTT_CLIENTID = "esp8266_ledStrip"
c = MQTTClient(MQTT_CLIENTID, MQTT_SERVER)
c.set_callback(sub_cb)
while True:
    try:
        c.connect()
        break
    except:
        print("ERROR: Failed to connect to MQTT Server " + MQTT_SERVER)
        time.sleep(1)
try:
    c.subscribe(MQTT_TOPIC)
except:
    print("ERROR: Failed to subscribe topic " + MQTT_TOPIC.decode())
    machine.reset()
led.on()

### Listen to MQTT
while True:
    try:
        c.wait_msg()  # Blocking wait for message
    except:
        pass
c.disconnect()
###

