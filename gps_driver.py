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
import subprocess
from time import sleep

# constantes pour le serial
DEVICE_NAME = '/dev/ttyGAUL0'
BAUD_RATE = 9600
SERIAL_TIMEOUT = 0
ser = serial.Serial(DEVICE_NAME, BAUD_RATE, timeout=SERIAL_TIMEOUT)

# prend en argument la string et retourne un dictionnaire 
# contenant le data formatté
def parse_gps_string(raw_data):
    dict_data = {}
    print(raw_data)
    s = raw_data.split(',')
    
    dict_data['header'] = s[0]
    
    # GGA - Global positioning System Fix Data
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
    # GLL - Latitude/Longitude
    elif dict_data['header'] == '$GPGLL':
        dict_data['latitude'] = float(s[1])
        dict_data['ns_indicator'] = s[2]
        dict_data['longitude'] = float(s[3])
        dict_data['ew_indicator'] = s[4]
        dict_data['utc_time'] = float(s[5])
        dict_data['status'] = s[6]
        dict_data['mode_indicator'], dict_data['checksum'] = s[-1].split('*')
    # GSA - GNSS DOP and Active Satellites
    elif dict_data['header'] == '$GPGSA':
        dict_data['mode'] = s[1]
        dict_data['fix_type'] = int(s[2])
        dict_data['satellites_used'] = [int(i) for i in s[3:-3] if i != '']
        dict_data['PDOP'] = float(s[-3])
        dict_data['HDOP'] = float(s[-2])
        t = s[-1].split('*')
        dict_data['VDOP'] = float(t[0])
        dict_data['checksum'] = int(t[1])
    # GSV - GNSS Satellites in View
    # TODO: parser le reste du data (selon le msg_number)
    elif dict_data['header'] == '$GPGSV':
        dict_data['msg_number'] = int(s[1])
        dict_data['sequence_number'] = int(s[2])
        dict_data['satellites_in_view'] = int(s[3])
        dict_data['satellite_id'] = int(s[4])
        dict_data['elevation'] = int(s[5])
        dict_data['azimuth'] = int(s[6])
        dict_data['SNR'] = int(s[7])
        dict_data['checksum'] = int(s[-1].split('*')[1])
    # RMC - Recommended Minimum Specific GNSS Data
    elif dict_data['header'] == '$GPRMC':
        dict_data['utc_time'] = s[1]
        dict_data['status'] = s[2]
        dict_data['latitude'] = float(s[3])
        dict_data['ns_indicator'] = s[4]
        dict_data['longitude'] = float(s[5])
        dict_data['ew_indicator'] = s[6]
        dict_data['speed_over_ground'] = float(s[7])
        dict_data['course_over_ground'] = float(s[8])
        dict_data['utc_date'] = s[9]
        dict_data['mode_indicator'], dict_data['checksum'] = s[-1].split('*')
    # VTG - Course Over Ground and Ground Speed
    elif dict_data['header'] == '$GPVTG':
        dict_data['course'] = float(s[1])
        dict_data['speed_knots'] = float(s[5])
        dict_data['speed_kmph'] = float(s[7])
        dict_data['mode_indicator'], dict_data['checksum'] = s[-1].split('*')
    else:
        print("GPS format not supported yet:\n{}".format(raw_data))
        return -1
    return dict_data


# TODO: vérifier que readline fonctionne avec les fins de ligne du GPS 
# TODO: vérifier qu'il faut .decode() avant d'envoyer la ligne
# TODO: vérifier que le with statement close le port comme il faut et qu'on 
#       peut le réutiliser
# lit une ligne de data du uart
def read_gps():
    global ser
    for i in range(10):
        line = ser.readline().decode()
        if line == '':
            #reset_uart_module()
            pass
        else:
            break
    else:
        return -1
    try:
        return parse_gps_string(line)
    except BaseException as e:
        print(e)

# ouvre le port serial, ne devrait pas être appellée à moins que la fonction 
# close ait été appellée avant
def open_port():
    global ser
    ser.open()


# ferme le port serial
def close_port():
    global ser
    ser.close()


# reset le kernel module du software UART
def reset_uart_module():
    close_port()
    r = subprocess.call(['sudo rmmod soft_uart'], shell=True)
    r = subprocess.call(['sudo insmod soft_uart-master/soft_uart.ko gpio_tx=22 gpio_rx=27'], shell=True)
    open_port()


if __name__ == '__main__':
    """
    s = b'$GPGGA,111636.932,2447.0949,N,12100.5223,E,1,11,0.8,118.2,M,,,,0000*02'
    p = parse_gps_string(s.decode())
    for k, v in p.items():
        print(k, ' : ', v)
    s = b'$GPGLL,2447.0944,N,12100.5213,E,112609.932,A,A*57'
    p = parse_gps_string(s.decode())
    for k, v in p.items():
        print(k, ' : ', v)
    s = b'$GPGSA,A,3,05,12,21,22,30,09,18,06,14,01,31,,1.2,0.8,0.9*36'
    p = parse_gps_string(s.decode())
    for k, v in p.items():
        print(k, ' : ', v)
    s = b'$GPGSV,3,1,12,05,54,069,45,12,44,061,44,21,07,184,46,22,78,289,47*72'
    p = parse_gps_string(s.decode())
    for k, v in p.items():
        print(k, ' : ', v)
    s = b'$GPRMC,111636.932,A,2447.0949,N,12100.5223,E,000.0,000.0,030407,,,A*61'
    p = parse_gps_string(s.decode())
    for k, v in p.items():
        print(k, ' : ', v)
    s = b'$GPVTG, 000.0,T,,M,000.0,N,0000.0,K,A*3D'
    p = parse_gps_string(s.decode())
    for k, v in p.items():
        print(k, ' : ', v)
    """
    for i in range(20):
        print(read_gps())
    close_port()
