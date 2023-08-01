# to run the script:
# python3 -m mp.mpfshell
# > open cu.usbserial-1420
# > put main.py

import machine
import time
import neopixel
import network
import socket
import WiFi_connect


#####################################
def RxData_network_handler(message):
    commands = message.split(';')
    print(commands)



def log(message):
    print(message)
    serverSock.sendto(message, (host_ipAddr, host_port))



def ledLights_01():
    while True:
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




#####################################
print('\r\nAppstar....................................')

leds_cnt = 60
leds_pin = 5    # GPIO5

leds = neopixel.NeoPixel(machine.Pin(leds_pin), leds_cnt)

UDP_PORT_NO = 11199



# Network connect
wlan = network.WLAN(network.STA_IF)
WiFi_connect.conn1(wlan)

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
myIPaddr = wlan.ifconfig()[0]
serverSock.bind((myIPaddr, UDP_PORT_NO))

print("Listening at: ", myIPaddr,":", UDP_PORT_NO)


#####################################
while True:
    ledLights_01()

    # data, host = serverSock.recvfrom(1024)
    # host_ipAddr = host[0]
    # host_port = host[1]

    # print("Rx from", host_ipAddr, ":", host_port)
    # # print("Data: ", data) 
    # RxData_network_handler(data.decode())

#####################################   end

