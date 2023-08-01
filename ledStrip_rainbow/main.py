# rainbow
import machine
import network
import time
import sys




def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return v, v, v
    i = int(h*6.0) # XXX assume int() truncates!
    f = (h*6.0) - i
    p = v*(1.0 - s)
    q = v*(1.0 - s*f)
    t = v*(1.0 - s*(1.0-f))
    i = i%6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q



print('\r\nAppstar....................................1')
print( "\t* System clock: ", machine.freq() / 1000000, "MHz")
pin_integratedLed = 2
led = machine.Pin(pin_integratedLed, machine.Pin.OUT)
led.off()
# Network connect
# wlan = network.WLAN(network.STA_IF)
# WiFi_connect.conn1(wlan)
led.on()


########################################### LED Strip
import neopixel


leds_cnt = 60
leds_pin = 4

leds = neopixel.NeoPixel(machine.Pin(leds_pin), leds_cnt)

SEPERATION = 60


#####################################
while True:

    for j in range(300):
        for i in range(leds.n):
            r,g,b = hsv_to_rgb(float(j)/float(50)+i/SEPERATION, 1, 1)
            leds[i] = (int(r*255), int(g*255), int(b*255))
        leds.write()
            # time.sleep(.1)

3