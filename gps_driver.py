"""

    @author:
        Maxime Guillemette
    
    @brief:
        Module de lecture des données GPS d'un Venus de Sparkfun
        
        Le format des strings du GPS est le suivant:
            $GPGGA,hhmmss.sss,ddmm.mmmm,a,dddmm.mmmm,a,x,xx,x.x,x.x,M,,,,xxxx*hh<CR><LF>
            
        Par exemple:
            $GPGGA,111636.932,2447.0949,N,12100.5223,E,1,11,0.8,118.2,M,,,,0000*02<CR><LF> 

"""

import serial


# constantes pour le serial
DEVICE_NAME = '/dev/ttySOFT0'
BAUD_RATE = 9600
SERIAL_TIMEOUT = 1


# prend en argument la string et retourne un dictionnaire 
# contenant le data formatté
def parse_gps_string(raw_data):
    dict_data = {}
    print(raw_data)
    s = raw_data.split(',')
    
    dict_data['header'] = s[0]
    
    if dict_data['header'] == '$GPGGA':
        dict_data['utc_time'] = float(s[1])
        dict_data['latitude'] = float(s[2])
        dict_data['ns_indicator'] = s[3]
        dict_data['longitude'] = float(s[4])
        dict_data['ew_indicator'] = s[5]
        dict_data['quality'] = int(s[6])
        dict_data['satellites_used'] = int(s[7])
        dict_data['HDOP'] = float(s[8])
        dict_data['altitude'] = float(s[9])
        dict_data['dgps_station_id'], dict_data['checksum'] = s[-1].split('*')
    elif dict_data['header'] == '$GPGLL':
        dict_data['latitude'] = float(s[1])
        dict_data['ns_indicator'] = s[2]
        dict_data['longitude'] = float(s[3])
        dict_data['ew_indicator'] = s[4]
        dict_data['utc_time'] = float(s[5])
        dict_data['status'] = s[6]
        dict_data['mode_indicator'], dict_data['checksum'] = s[-1].split('*')
    else:
        print("GPS format not supported yet")
        return -1
    
    return dict_data


# TODO: vérifier que readline fonctionne avec les fins de ligne du GPS 
# TODO: vérifier qu'il faut .decode() avant d'envoyer la ligne
# TODO: vérifier que le with statement close le port comme il faut et qu'on 
#       peut le réutiliser
# lit une ligne de data du uart
def read_gps():
    with serial.Serial(DEVICE_NAME, BAUD_RATE, timeout=SERIAL_TIMEOUT) as ser:
        line = ser.readline()
        return parse_gps_string(line)


if __name__ == '__main__':
    s = b'$GPGGA,111636.932,2447.0949,N,12100.5223,E,1,11,0.8,118.2,M,,,,0000*02'
    print(parse_gps_string(s.decode()))
    s = b'$GPGLL,2447.0944,N,12100.5213,E,112609.932,A,A*57'
    print(parse_gps_string(s.decode()))
