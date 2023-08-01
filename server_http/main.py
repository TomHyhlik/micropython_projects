import socket
import machine

import network
import time
import sys
import urequests

import WiFi_connect

import utils
    
serverPort = 8080
pin_integratedLed = 2
§

####################### MAIN  ####################
def main():
  # print system info
  print('\r\nAppstar....................................')
  print( "\t* System clock: ", machine.freq() / 1000000, "MHz")
    
    
  # init peripherals
  led = machine.Pin(pin_integratedLed, machine.Pin.OUT)
  led.on()

  # Network connect
  wlan = network.WLAN(network.STA_IF)
  WiFi_connect.conn1(wlan)



  s = socket.socket()
  ai = socket.getaddrinfo(wlan.ifconfig()[0], serverPort)
  addr = ai[0][-1]
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind(addr)
  s.listen(5)
  print("Server accessible at http://", wlan.ifconfig()[0],":",serverPort,"/", sep='')


  ################ LOOP ##################
  counter = 0
  while True:

      res = s.accept()
      client_s = res[0]
      client_addr = res[1]
      print("Client address:", client_addr)
      print("Client socket:", client_s)

      led.off()
      req = client_s.recv(4096)
      led.on()

      print("Request:")
      print(req)

      print
      if str(req).find('pica') >= 0:
        client_s.send(utils.CONTENT2)
        led.off()
        time.sleep(1)
        led.on()
      else:
        client_s.send(utils.CONTENT % counter)

      client_s.close()
      counter += 1
      print()

  ################# END LOOP ##################

if __name__ == "__main__":
    main()


