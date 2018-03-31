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

# prend en argument la string et retourne un dictionnaire 
# contenant le data formatté
def parse_gps_string(raw_data):
    dict_data = {}
    s = raw_data.split(',')
    
    dict_data['header'] = s[0]
    dict_data['utc_time'] = s[1]
    dict_data['latitude'] = s[2]
    dict_data['ns_indicator'] = s[3]
    dict_data['longitude'] = s[4]
    dict_data['ew_indicator'] = s[5]
    dict_data['quality'] = s[6]
    dict_data['satellites_used'] = s[7]
    dict_data['HDOP'] = s[8]
    dict_data['altitude'] = s[9]
    dict_data['dgps_station_id'], dict_data['checksum'] = s[-1].split('*')
    
    return dict_data



if __name__ == '__main__':
    s = '$GPGGA,111636.932,2447.0949,N,12100.5223,E,1,11,0.8,118.2,M,,,,0000*02'
    print(parse_gps_string(s))
    
