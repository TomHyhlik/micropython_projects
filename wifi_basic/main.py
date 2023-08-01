

#####################################################

#########################   Main    ####################

import machine
import time

import network
import WiFi_connect


print('\r\nAppstar....................................')

# Network connect
wlan = network.WLAN(network.STA_IF)
WiFi_connect.conn1(wlan)

pin_integratedLed_number = 2
secondsCnt = 0

pin_integratedLed = machine.Pin(pin_integratedLed_number, machine.Pin.OUT)

while True:
    pin_integratedLed.off()
    time.sleep(.2) 

    pin_integratedLed.on()
    time.sleep(.2) 
    
    secondsCnt = secondsCnt + 1
    print('Alive:', secondsCnt)










