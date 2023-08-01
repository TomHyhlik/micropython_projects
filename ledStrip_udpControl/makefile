# USAGE:
# This makefile loads the main.py to the micropython device
# the script starts running by reseting the micropython device
# you can do this manually by entering the following lines bellow to terminal
# python3 -m mp.mpfshell
# > open cu.usbserial-1420
# > put main.py

CC = python3
CC_PARAM = -m mp.mpfshell

DEVICENAME = "cu.usbserial-1420"


FILES = $(wildcard *.py)
CMD_PUTFILES := $(foreach file,$(FILES), put $(file) \n)
CMD_OPEN = "open $(DEVICENAME)"


SCRIPT_INPUT = " \
	$(CMD_OPEN) \n \
	$(CMD_PUTFILES) \n \
	exit\n \
	"

all:
	cp ../lib/WiFi_connect.py ./
	echo $(SCRIPT_INPUT) | $(CC) $(CC_PARAM)
	termik -c serial -n $(DEVICENAME)



open:
	echo $(CMD_OPEN) | $(CC) $(CC_PARAM)
	ls

