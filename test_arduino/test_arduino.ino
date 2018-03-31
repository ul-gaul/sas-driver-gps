/*
 * programme pour tester le software serial sur le Raspberry Pi 3B du GAUL
 */

#include "Arduino.h"


#define BAUD_RATE 4800

unsigned char s[] = "gaul serial test\n";
int bytes_available = 0;

void setup() {
    Serial.begin(4800);
    Serial2.begin(BAUD_RATE);
}


void loop() {
    for(int i = 0; i < strlen((char *) s); i++) {
	Serial2.write(s[i] + 160);
    }
    bytes_available = Serial2.available();
    if (bytes_available) {
        for (int i = 0; i < bytes_available; i++) {
            int b = Serial2.read();
            Serial.write(b + 160);
        }
        Serial.println("\nfin");
    } else { 
        delay(500);
    }
}
