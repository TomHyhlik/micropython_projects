import machine
import network
import time
import sys

import WiFi_connect

# print system info
print('\r\nAppstar....................................1')
print( "\t* System clock: ", machine.freq() / 1000000, "MHz")
pin_integratedLed = 2


# init peripherals
led = machine.Pin(pin_integratedLed, machine.Pin.OUT)
led.on()

# Network connect
wlan = network.WLAN(network.STA_IF)
WiFi_connect.conn1(wlan)


#############################
from umqtt.simple import MQTTClient
import ubinascii

def sub_cb(topic, msg): 
   print(msg) 

CLIENT_ID = ubinascii.hexlify(machine.unique_id())
SERVER = "10.0.0.182"


client = MQTTClient(CLIENT_ID, SERVER)
client.set_callback(sub_cb) 

while True:
    try:
        client.connect()
        break
    except:
        print("ERROR: Failed to connect MQTT client")
        time.sleep(10)

client.subscribe(topic="hiTx") 


val = 0
while True: 
    print("Sending message: " + str(val)) 
    client.publish(topic="hi", msg=str(val))
    val += 1
    time.sleep(1) 



#############################
aliveCtr = 0    
counter = 0
while True:
    print("ALIVE: " +  str(aliveCtr))
    aliveCtr += 1
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)

#############################