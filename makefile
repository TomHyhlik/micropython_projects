# this programming script uses ampy


# PROJECTNAME = ledStrip_rainbow
PROJECTNAME = ledStrip_audioControl
DEVICENAME = ttyUSB0




CC = ampy


all: flash run


flash:
	$(CC) --port /dev/$(DEVICENAME) put ./$(PROJECTNAME)/*.py
	# $(CC) --port /dev/$(DEVICENAME) put ./lib/WiFi_connect.py 
	# $(CC) --port /dev/$(DEVICENAME) put ./lib/known_networks_data.py 



run:
	termik -conn serial -pname $(DEVICENAME) -baud 115200

