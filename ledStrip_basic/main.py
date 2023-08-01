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




def ledLights_01():
    for  i in range(leds_cnt):
        leds[i] = ( 0, 0, 255)
        leds.write()
        time.sleep(0.05)

    for  i in range(leds_cnt):
        leds[i] = ( 255, 0, 0)
        leds.write()
        time.sleep(0.05)

    for  i in range(leds_cnt):
        leds[i] = ( 0, 255, 0)
        leds.write()
        time.sleep(0.05)

####################################
def ledLights_cycle():
    n = leds.n
    ledsLights_clear()

    repeats = 1

    for i in range(n * repeats):
        for k in range(n):
            leds[k] = (0, 0, 0)
        leds[i % n] = (255, 255, 255)
        leds.write()
        time.sleep_ms(25)

    for i in range(n * repeats):
        for k in range(n):
            leds[k] = (0, 0, 0)
        for spaceBetween in range(0, 20, 10):
            leds[(i + spaceBetween) % n] = (255, 255, 255)
        leds.write()
        time.sleep_ms(25)

    for i in range(n * repeats):
        for k in range(n):
            leds[k] = (0, 0, 0)
        for spaceBetween in range(0, 20, 10):
            leds[(i + spaceBetween) % n] = (255, 255, 255)
        leds.write()
        time.sleep_ms(25)

    repeats = 5
    for i in range(n * repeats):
        for k in range(n):
            leds[k] = (0, 0, 0)
        for spaceBetween in range(0, n, 10):
            leds[(i + spaceBetween) % n] = (255, 255, 255)
        leds.write()
        time.sleep_ms(25)

    repeats = 5
    for i in range(n * repeats):
        for k in range(n):
            leds[k] = (0, 0, 0)
        for spaceBetween in range(0, n, 5):
            leds[(i + spaceBetween) % n] = (255, 255, 255)
        leds.write()
        time.sleep_ms(25)

    repeats = 3
    for i in range(n * repeats):
        for k in range(n):
            leds[k] = (0, 0, 0)
        for spaceBetween in range(0, n, 5):
            if (spaceBetween % 10) == 0:
                leds[(i + spaceBetween) % n] = (255, 0, 0)
            if (spaceBetween % 15) == 0:
                leds[(i + spaceBetween) % n] = (0, 255, 0)
            if (spaceBetween % 20) == 0:
                leds[(i + spaceBetween) % n] = (0, 0, 255)
        leds.write()
        time.sleep_ms(25)

    repeats = 8
    for i in range(n * repeats):
        for k in range(n):
            leds[k] = (0, 0, 0)
        for spaceBetween in range(0, n, 5):
            if (spaceBetween % 1) == 0:
                leds[(i + spaceBetween) % n] = (0, 255, 0)
            if (spaceBetween % 2) == 0:
                leds[(i + spaceBetween) % n] = (10, 255, 50)
            if (spaceBetween % 3) == 0:
                leds[(i + spaceBetween) % n] = (0, 255, 20)
            if (spaceBetween % 4) == 0:
                leds[(i + spaceBetween) % n] = (255, 255, 0)
        leds.write()
        time.sleep_ms(25)


    repeats = 8
    for i in range(n * repeats):
        for k in range(n):
            leds[k] = (0, 0, 0)
        for spaceBetween in range(0, n, 5):
            if (spaceBetween % 1) == 0:
                leds[(i + spaceBetween) % n] = (0, 255, 0)
            if (spaceBetween % 2) == 0:
                leds[(i + spaceBetween) % n] = (10, 255, 50)
            if (spaceBetween % 3) == 0:
                leds[(i + spaceBetween) % n] = (50, 255, 10)
            if (spaceBetween % 4) == 0:
                leds[(i + spaceBetween) % n] = (255, 255, 10)
        leds.write()
        time.sleep_ms(25)

########################### green sequence
    for b in range(10):
        repeats = 1
        for i in range(n * repeats):
            for k in range(n):
                leds[k] = (0, 0, 0)
            for spaceBetween in range(0, n, 5):
                if (spaceBetween % 1) == 0:
                    leds[(i + spaceBetween) % n] = (255, 255, 0)
                if (spaceBetween % 2) == 0:
                    leds[(i + spaceBetween) % n] = (100, 255, 0)
                if (spaceBetween % 3) == 0:
                    leds[(i + spaceBetween) % n] = (50, 255, 10)
                if (spaceBetween % 4) == 0:
                    leds[(i + spaceBetween) % n] = (255, 100, 0)
            leds.write()
            time.sleep_ms(25)
        for i in range(n * repeats):
            for k in range(n):
                leds[k] = (0, 5, 0)
            for spaceBetween in range(0, n, 5):
                if (spaceBetween % 1) == 0:
                    leds[(i + spaceBetween) % n] = (255, 255, 0)
                if (spaceBetween % 2) == 0:
                    leds[(i + spaceBetween) % n] = (100, 255, 0)
                if (spaceBetween % 3) == 0:
                    leds[(i + spaceBetween) % n] = (50, 255, 10)
                if (spaceBetween % 4) == 0:
                    leds[(i + spaceBetween) % n] = (255, 100, 0)
            leds.write()
            time.sleep_ms(25)
        for i in range(n * repeats):
            for k in range(n):
                leds[k] = (8, 10, 0)
            for spaceBetween in range(0, n, 5):
                if (spaceBetween % 1) == 0:
                    leds[(i + spaceBetween) % n] = (255, 255, 0)
                if (spaceBetween % 2) == 0:
                    leds[(i + spaceBetween) % n] = (100, 255, 0)
                if (spaceBetween % 3) == 0:
                    leds[(i + spaceBetween) % n] = (50, 255, 10)
                if (spaceBetween % 4) == 0:
                    leds[(i + spaceBetween) % n] = (255, 100, 0)
            leds.write()
            time.sleep_ms(25)



    for b in range(10):
        repeats = 1
        for i in range(n * repeats):
            for k in range(n):
                leds[k] = (0, 0, 0)
            for spaceBetween in range(0, n, 5):
                if (spaceBetween % 1) == 0:
                    leds[(i + spaceBetween) % n] = (255, 20, 0)
                if (spaceBetween % 2) == 0:
                    leds[(i + spaceBetween) % n] = (255, 80, 10)
                if (spaceBetween % 3) == 0:
                    leds[(i + spaceBetween) % n] = (255, 20, 20)
                if (spaceBetween % 4) == 0:
                    leds[(i + spaceBetween) % n] = (255, 0, 100)
            leds.write()
            time.sleep_ms(25)
        for i in range(n * repeats):
            for k in range(n):
                leds[k] = (10, 0, 0)
            for spaceBetween in range(0, n, 5):
                if (spaceBetween % 1) == 0:
                    leds[(i + spaceBetween) % n] = (255, 20, 0)
                if (spaceBetween % 2) == 0:
                    leds[(i + spaceBetween) % n] = (255, 80, 10)
                if (spaceBetween % 3) == 0:
                    leds[(i + spaceBetween) % n] = (255, 20, 20)
                if (spaceBetween % 4) == 0:
                    leds[(i + spaceBetween) % n] = (255, 0, 100)
            leds.write()
            time.sleep_ms(25)


    repeats = 8
    for i in range(n * repeats):
        for k in range(n):
            leds[k] = (0, 0, 0)
        for spaceBetween in range(0, n, 5):
            if (spaceBetween % 1) == 0:
                leds[(i + spaceBetween) % n] = (255, 100, 0)
            if (spaceBetween % 2) == 0:
                leds[(i + spaceBetween) % n] = (255, 80, 10)
            if (spaceBetween % 3) == 0:
                leds[(i + spaceBetween) % n] = (255, 20, 80)
            if (spaceBetween % 4) == 0:
                leds[(i + spaceBetween) % n] = (255, 0, 100)
        leds.write()
        time.sleep_ms(25)


    repeats = 3
    for i in range(n * repeats):
        for k in range(n):
            leds[k] = (0, 0, 0)
        for spaceBetween in range(0, n, 5):
            if (spaceBetween % 1) == 0:
                leds[(i + spaceBetween) % n] = (255, 100, 0)
            if (spaceBetween % 2) == 0:
                leds[(i + spaceBetween) % n] = (255, 200, 10)
            if (spaceBetween % 3) == 0:
                leds[(i + spaceBetween) % n] = (255, 200, 100)
            if (spaceBetween % 4) == 0:
                leds[(i + spaceBetween) % n] = (255, 100, 100)
        leds.write()
        time.sleep_ms(25)

    repeats = 5
    for i in range(n * repeats):
        for k in range(n):
            leds[k] = (0, 0, 0)
        for spaceBetween in range(0, n, 5):
            if (spaceBetween % 1) == 0:
                leds[(i + spaceBetween) % n] = (255, 255, 0)
            if (spaceBetween % 2) == 0:
                leds[(i + spaceBetween) % n] = (255, 100, 0)
            if (spaceBetween % 3) == 0:
                leds[(i + spaceBetween) % n] = (255, 50, 10)
            if (spaceBetween % 4) == 0:
                leds[(i + spaceBetween) % n] = (255, 50, 50)
        leds.write()
        time.sleep_ms(25)

########################## red - yellow sequence

    # for b in range(2):
    #     repeats = 1
    #     for i in range(n * repeats):
    #         for k in range(n):
    #             leds[k] = (5, 5, 5)
    #         for spaceBetween in range(0, n, 5):
    #             if (spaceBetween % 1) == 0:
    #                 leds[(i + spaceBetween) % n] = (255, 100, 0)
    #             if (spaceBetween % 2) == 0:
    #                 leds[(i + spaceBetween) % n] = (255, 0, 0)
    #             if (spaceBetween % 3) == 0:
    #                 leds[(i + spaceBetween) % n] = (255, 0, 100)
    #             if (spaceBetween % 4) == 0:
    #                 leds[(i + spaceBetween) % n] = (255, 0, 50)
    #         leds.write()
    #         time.sleep_ms(25)
    #     for i in range(n * repeats):
    #         for k in range(n):
    #             leds[k] = (10, 0, 0)
    #         for spaceBetween in range(0, n, 5):
    #             if (spaceBetween % 1) == 0:
    #                 leds[(i + spaceBetween) % n] = (255, 100, 0)
    #             if (spaceBetween % 2) == 0:
    #                 leds[(i + spaceBetween) % n] = (255, 0, 0)
    #             if (spaceBetween % 3) == 0:
    #                 leds[(i + spaceBetween) % n] = (255, 0, 100)
    #             if (spaceBetween % 4) == 0:
    #                 leds[(i + spaceBetween) % n] = (255, 0, 50)
    #         leds.write()
    #         time.sleep_ms(25)
    #     for i in range(n * repeats):
    #         for k in range(n):
    #             leds[k] = (5, 5, 0)
    #         for spaceBetween in range(0, n, 5):
    #             if (spaceBetween % 1) == 0:
    #                 leds[(i + spaceBetween) % n] = (255, 100, 0)
    #             if (spaceBetween % 2) == 0:
    #                 leds[(i + spaceBetween) % n] = (255, 0, 0)
    #             if (spaceBetween % 3) == 0:
    #                 leds[(i + spaceBetween) % n] = (255, 0, 100)
    #             if (spaceBetween % 4) == 0:
    #                 leds[(i + spaceBetween) % n] = (255, 0, 50)
    #         leds.write()
    #         time.sleep_ms(25)



########################## blue sequence
    for b in range(10):
        repeats = 1
        for i in range(n * repeats):
            for k in range(n):
                leds[k] = (0, 0, 0)
            for spaceBetween in range(0, n, 5):
                if (spaceBetween % 1) == 0:
                    leds[(i + spaceBetween) % n] = (100, 10, 255)
                if (spaceBetween % 2) == 0:
                    leds[(i + spaceBetween) % n] = (255, 100, 255)
                if (spaceBetween % 3) == 0:
                    leds[(i + spaceBetween) % n] = (0, 0, 255)
                if (spaceBetween % 4) == 0:
                    leds[(i + spaceBetween) % n] = (255, 40, 50)
            leds.write()
            time.sleep_ms(25)
        for i in range(n * repeats):
            for k in range(n):
                leds[k] = (0, 0, 5)
            for spaceBetween in range(0, n, 5):
                if (spaceBetween % 1) == 0:
                    leds[(i + spaceBetween) % n] = (100, 10, 255)
                if (spaceBetween % 2) == 0:
                    leds[(i + spaceBetween) % n] = (255, 100, 255)
                if (spaceBetween % 3) == 0:
                    leds[(i + spaceBetween) % n] = (0, 0, 255)
                if (spaceBetween % 4) == 0:
                    leds[(i + spaceBetween) % n] = (255, 40, 50)
            leds.write()
            time.sleep_ms(25)
        for i in range(n * repeats):
            for k in range(n):
                leds[k] = (5, 5, 5)
            for spaceBetween in range(0, n, 5):
                if (spaceBetween % 1) == 0:
                    leds[(i + spaceBetween) % n] = (100, 10, 255)
                if (spaceBetween % 2) == 0:
                    leds[(i + spaceBetween) % n] = (255, 100, 255)
                if (spaceBetween % 3) == 0:
                    leds[(i + spaceBetween) % n] = (0, 0, 255)
                if (spaceBetween % 4) == 0:
                    leds[(i + spaceBetween) % n] = (255, 40, 50)
            leds.write()
            time.sleep_ms(25)




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
leds_pin = 5    # GPIO5

leds = neopixel.NeoPixel(machine.Pin(leds_pin), leds_cnt)


#####################################
while True:
    ledLights_fade()
    ledLights_cycle()




#####################################   end


