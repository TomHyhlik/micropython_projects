# micropython_projects
Hobby micropython projects running on ESP8266


## Setup
In the directory "install" are scripts to erase and flash the micropython to the device.
Flashing the program to the device is done via makefile.



## Project 

### Led Strip Audio Control
Audio-controlled led strip. The leds stip creates visual effect based on the sounds.
The purpose is to create a decoration lighting for a playing music.

#### Parts

* ESP266 placed on the Node MCU board
* Led Strip WS2812B
* Microphone

#### Pinout
| Periphery                     | ESP8266        | Node MCU PCB |
| ----------------------------- | -------------- | -------------|
| Microphone Analog output      | ADC0 			 | A1 			|
| WS2812B						| GPIO5		 | D1			|
| Debug pin output      		| GPIO16		 | D0			|



