# to run the script:
# python3 -m mp.mpfshell
# > open cu.usbserial-1420
# > put main.py

import machine
import time
import neopixel


def ledsLights_clear():
    n = leds.n
    for i in range(n):
        leds[i] = (0, 0, 0)
    leds.write()



####################################
def ledLights_cycle():
    n = leds.n
    # ledsLights_clear()

    blue = 0
    for i in range(n):
        if i < n/2:
            blue += 5
        else:     
            blue -= 5
        leds[i] = (255, 255, blue)
    leds.write()



    # i = 0
    # while i < n:
    #     leds[i] = (255, 255, 50)
    #     i += 1

 
 






# ####################################
# def ledLights_bounce():
#     n = leds.n
#     for i in range(4 * n):
#         for j in range(n):
#             leds[j] = (0, 255, 10)
#         if (i // n) % 2 == 0:
#             leds[i % n] = (255, 0, 0)
#         else:
#             leds[n - 1 - (i % n)] = (255, 0, 0)
#         leds.write()
#         time.sleep_ms(20)

# #####################################
def ledLights_fade():
    n = leds.n
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            leds[j] = (0, val, 0)
        leds.write()
#     for i in range(0, 4 * 256, 8):
#         for j in range(n):
#             if (i // 256) % 2 == 0:
#                 val = i & 0xff
#             else:
#                 val = 255 - (i & 0xff)
#             leds[j] = (val, val, 0)
#         leds.write()
#     for i in range(0, 4 * 256, 8):
#         for j in range(n):
#             if (i // 256) % 2 == 0:
#                 val = i & 0xff
#             else:
#                 val = 255 - (i & 0xff)
#             leds[j] = (0, val, 0)
#         leds.write()
#     for i in range(0, 4 * 256, 8):
#         for j in range(n):
#             if (i // 256) % 2 == 0:
#                 val = i & 0xff
#             else:
#                 val = 255 - (i & 0xff)
#             leds[j] = (0, val, val)
#         leds.write()
#     for i in range(0, 4 * 256, 8):
#         for j in range(n):
#             if (i // 256) % 2 == 0:
#                 val = i & 0xff
#             else:
#                 val = 255 - (i & 0xff)
#             leds[j] = (0, 0, val)
#         leds.write()
#     for i in range(0, 4 * 256, 8):
#         for j in range(n):
#             if (i // 256) % 2 == 0:
#                 val = i & 0xff
#             else:
#                 val = 255 - (i & 0xff)
#             leds[j] = (val, 0, val)
#         leds.write()
# #####################################










#####################################
print('\r\nAppstar....................................')

leds_cnt = 60
leds_pin = 4

leds = neopixel.NeoPixel(machine.Pin(leds_pin), leds_cnt)

ledLights_cycle()

aliveCnt = 0
#####################################
while True:
    print("Alive: ", aliveCnt)
    aliveCnt += 1
    time.sleep(1)
    # ledLights_fade()
    ledLights_cycle()




#####################################   end


