# rainbow
import machine
# import network
import time
import sys
import neopixel



# Function to convert color encoding hsv to rgb
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



pin_ledStrip = 15
# pin_integratedLed = 2
pin_debug = 16

print('\r\nAppstar....................................1')
machine.freq(160000000)
print( "\t* System clock: ", machine.freq() / 1000000, "MHz")

pinDebug = machine.Pin(pin_debug, machine.Pin.OUT)
pinDebug.off()
pinDebug.on()


# LED Strip
ledStrip_leds_cnt = 60
ledStrip = neopixel.NeoPixel(machine.Pin(pin_ledStrip), ledStrip_leds_cnt)


# microphone
microphone = machine.ADC(0)


######### Config 
maxLedsOn = 4
microphoneSensitivity = 150.0

microphoneSensitivity_range_top = 150.0
microphoneSensitivity_range_bottom = 1.0


# Globals
ticks = time.ticks_ms()
h = 0.0
s = 0.0
v = 0.0

lastOn_0_index = 0
lastOn_1_index = 0

current_h = 0.0

# leds on coeficient
current_ledsOn_coef = 0

variance = 0.0
variance_synced = 0.0

microphoneSamples = [ 0 ]

#####################################
while True:
    
    # Debug pin switch
    pinDebug.off()
    pinDebug.on()


    # # # Read Microphone
    sample = microphone.read()


    # Get variance of the actual value
    # get average from previous microphone samples
    average = sum(microphoneSamples) / len(microphoneSamples)
    # add the new microphone sample to the buffer
    if len(microphoneSamples) > 5:
        del microphoneSamples[0]
    microphoneSamples.append(sample)
    # calculate variance
    variance = abs(average - sample) / 1024.0
    variance_synced = variance * microphoneSensitivity
    if variance_synced < 0.03:
        variance_synced = 0.0


    # Update hsv values
    h = current_h
    s = 1
    v = variance_synced
    r,g,b = hsv_to_rgb(h, s, v)
    # # print('(hsv)=()',h,',',s,',',v,'')


    # Write the LEDs
    r_int = int(r*255)
    g_int = int(g*255)
    b_int = int(b*255)
    # clear the written led in the previous cycle
    ledStrip[lastOn_0_index] = (0, 0, 0)
    # Set on multiple leds if variance_synced is big
    if (variance_synced > 0.5):
        # write multiple leds
        # check index to prevent overflow
        if (lastOn_1_index + maxLedsOn >= ledStrip_leds_cnt):
            lastOn_1_index = ledStrip_leds_cnt - maxLedsOn - 1
        for i in range(maxLedsOn):
            ledStrip[lastOn_1_index + i] = (r_int, g_int, b_int)
        current_ledsOn_coef += 1
    else:
        # write only 1 led    
        ledStrip[lastOn_1_index] = (r_int, g_int, b_int)
        current_ledsOn_coef = 0
    ledStrip.write()


    # update microphone sensitivity
    if (current_ledsOn_coef > 0):
        # decrease sensitivity
        microphoneSensitivity *= (0.99 - (current_ledsOn_coef * 0.003))
        if (microphoneSensitivity < microphoneSensitivity_range_bottom):
            microphoneSensitivity = microphoneSensitivity_range_bottom
    else:
        # increase sensitivity
        microphoneSensitivity *= 1.001
        if (microphoneSensitivity > microphoneSensitivity_range_top):
            microphoneSensitivity = microphoneSensitivity_range_top
    # print("micSens: ", microphoneSensitivity)


    # Generate the index and color of the next LED
    # Get random nuber
    ticks = time.ticks_ms()
    # print("ticks: ", ticks)
    lastOn_0_index = lastOn_1_index
    lastOn_1_index = ticks % ledStrip_leds_cnt
    current_h = (ticks % 100) * 0.006 + 0.4
    # print("lastOn_0_index: ", lastOn_0_index)


    # time.sleep(1)