
#           CONFIG          ################################
PORT_NAME=/dev/ttyUSB0
CC_ESPTOOL=../../esptool/esptool.py
BINARY_MICROPYTHON=./esp8266-20230426-v1.20.0.bin

############################################################


# download esptool
# git clone https://github.com/espressif/esptool/ ../../esptool

# get chip details
python3 $CC_ESPTOOL --port $PORT_NAME chip_id

# echo "############################################################"
# echo "# Erase flash"
# echo "############################################################"
# python3 $CC_ESPTOOL --port $PORT_NAME erase_flash

echo "############################################################"
echo "# Writing micropython image"
echo "############################################################"
python3 $CC_ESPTOOL --port $PORT_NAME --baud 460800 write_flash --flash_size=detect 0 $BINARY_MICROPYTHON
