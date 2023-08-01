# rainbow
import machine
# import network
import time
import sys
import neopixel




def hsv_to_rgb(h, s, v):
    if v > 1.0:
        v = 1.0
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



pin_ledStrip = 4
pin_integratedLed = 2
pin_PIR =   0


print('\r\nAppstar....................................1')
print( "\t* System clock: ", machine.freq() / 1000000, "MHz")
led = machine.Pin(pin_integratedLed, machine.Pin.OUT)
led.off()
# Network connect
# wlan = network.WLAN(network.STA_IF)
# WiFi_connect.conn1(wlan)
led.on()


########################################### LED Strip
leds_cnt = 60
leds = neopixel.NeoPixel(machine.Pin(pin_ledStrip), leds_cnt)
SEPERATION = 60
leds_intensity = 0.1


########################################### PIR callback
from machine import Pin
pir = Pin(pin_PIR, Pin.IN)
PIR_Callback_ctr = 0

def PIR_Callback(p):
    global leds_intensity
    global PIR_Callback_ctr
    PIR_Callback_ctr += 1
    leds_intensity = 2
    print("PIR_Callback_Ctr: ", PIR_Callback_ctr)
    # print('pin change', p)
    # led.off()


pir.irq(trigger=Pin.IRQ_RISING, handler=PIR_Callback)
# pir.irq(trigger=Pin.IRQ_FALLING, handler=PIR_Callback)


#####################################
while True:

    for j in range(300):
        for i in range(leds.n):
            r,g,b = hsv_to_rgb(float(j)/float(50)+i/SEPERATION, 1, leds_intensity)
            leds[i] = (int(r*255), int(g*255), int(b*255))
        leds.write()
        # time.sleep(.1)

        if leds_intensity > 0.01:
            leds_intensity *= 0.999

        # print('Intensity: ', leds_intensity)