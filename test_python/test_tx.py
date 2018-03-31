"""

    @author:
        Maxime Guillemette
    
    @brief:
        Fichier de test de transmission pour le GAUL

"""

import serial
from time import sleep

str_test = b'test gaul 2018 ALLO'

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttySOFT0', 9600, timeout=1)
    while True:
        ser.write(str_test)
        sleep(1)
        print(ser.read(len(str_test)))
