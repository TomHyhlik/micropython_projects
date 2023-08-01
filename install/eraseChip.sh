
#           CONFIG          ################################
PORT_NAME=/dev/ttyUSB0
CC_ESPTOOL=../../esptool/esptool.py

############################################################


# echo "############################################################"
# echo "# Erase flash"
# echo "############################################################"
python3 $CC_ESPTOOL --port $PORT_NAME erase_flash
