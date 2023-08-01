import socket
import machine
from machine import Pin, ADC

import network
import time
import sys
import urequests

from machine import I2C
from bmp280 import BMP280

import WiFi_connect
    
serverPort = 8080
pin_integratedLed = 2

pin_BMP280_scl = 5
pin_BMP280_sda = 4



####################### MAIN  ####################
def main():
  # print system info
  print('\r\nAppstar....................................')
  print( "\t* System clock: ", machine.freq() / 1000000, "MHz")
    
    
  # init peripherals
  led = machine.Pin(pin_integratedLed, machine.Pin.OUT)
  led.on()

  pin_analog_01 = 0
  pot = ADC(pin_analog_01)

  # temperature sensor
  bus = I2C(scl=machine.Pin(pin_BMP280_scl), sda=machine.Pin(pin_BMP280_sda))

  # Network connect
  wlan = network.WLAN(network.STA_IF)
  WiFi_connect.conn1(wlan)



  UDP_IP_ADDRESS = "192.168.8.108"

  UDP_PORT_NO = 1337
  clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  i = 0


  while True:
    try:
      bme = bme280.BME280(i2c=i2c)
      print(bme.values)
    except:
      print("Sensor not connected\n")

    try:
      bmp = BMP280(bus)
      temperature = bmp.temperature
      pressure = bmp.pressure
    except:
      print('Sensor not connected')

      
    Message = "{\"MessageCnt\":" + str(i) + ", \"temperature\": " + str(temperature) + ", \"pressure\" :" + str(pressure) +", \"potValue\": " + str(pot.read()) + "}"

    clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))
    print("\n_________________________________________________\n", "UDP_message: ", Message, "\nUDP_destination", UDP_IP_ADDRESS, ": ", UDP_PORT_NO)
    time.sleep(2)
    i += 1 

  ################# END LOOP ##################



if __name__ == "__main__":
    main()


