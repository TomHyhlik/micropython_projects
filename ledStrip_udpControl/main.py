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
    for cmd_str in commands:
        try:
            cmd = cmd_str.split('=')
            if len(cmd) == 2:
                ledID = int(cmd[0])
                ledData = cmd[1].split(',')
                if len(ledData) == 3:
                    led_r = int(ledData[0])
                    led_g = int(ledData[1])
                    led_b = int(ledData[2])
                    leds[ledID] = (led_r, led_g, led_b)
                    # print("Setting ", ledID, "=", "(", led_r,",", led_g, ",", led_b, ")")
                    log("Setting: " + cmd_str)
                    continue
        except:
            pass
        errorMessage = "Failed to parse:" + cmd_str
        log(errorMessage)
    leds.write()





def log(message):
    print(message)
    serverSock.sendto(message, (host_ipAddr, host_port))







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
    data, host = serverSock.recvfrom(1024)
    host_ipAddr = host[0]
    host_port = host[1]

    print("Rx from", host_ipAddr, ":", host_port)
    # print("Data: ", data) 
    RxData_network_handler(data.decode())

#####################################   end

