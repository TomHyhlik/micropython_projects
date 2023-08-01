

#####################################################

#########################   Main    ####################

import machine
import time

print('\r\nAppstar....................................')

pin_integratedLed_number = 2
secondsCnt = 0

pin_integratedLed = machine.Pin(pin_integratedLed_number, machine.Pin.OUT)

while True:
    pin_integratedLed.off()
    time.sleep(.5)

    pin_integratedLed.on()
    time.sleep(.5)
    
    secondsCnt = secondsCnt + 1
    print('Alive:', secondsCnt)










