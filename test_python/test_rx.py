"""

    @author:
        Maxime Guillemette
    
    @brief:
        Fichier de test de transmission pour le GAUL

"""

import serial

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttySOFT0', 9600, timeout=1)
    while True:
        print(ser.read())
    
