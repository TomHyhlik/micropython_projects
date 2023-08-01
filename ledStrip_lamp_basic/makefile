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




SCRIPT_INPUT = "open $(DEVICENAME) \nput main.py \nexit"

all:
	echo $(SCRIPT_INPUT) | $(CC) $(CC_PARAM)
	# termik -c serial -n $(DEVICENAME)
