/*
#****************************************************************************************************************************
#   --------------------------------------------------------------------------------------------------------------------
#   @Autecla: Simulating the RFID_Module
#   Sketch/program to send data by UART_serial to ESP32, in order to simulate the RFID_Module
#   Arduino Port:
#     Pin_RX = 2
#     Pin_TX = 3
#   --------------------------------------------------------------------------------------------------------------------
#****************************************************************************************************************************
*/

#include <SoftwareSerial.h>

SoftwareSerial sw(2, 3); // RX, TX
char j = '1';

void setup() {
 Serial.begin(9600);
 Serial.println("Interfacfing arduino with ESP32");
 Serial.println("Simulating the RFID_Module");
 sw.begin(9600);
}

void loop() {
  if(j == '1'){
    sw.print("M1P1C1C2C5C8");
    sw.println();
    delay(2000);
    sw.print("M2P3C1C2C5C8");
    sw.println();
    delay(2000);
    sw.print("M3P2C1C2C5C8");
    sw.println();
    delay(2000);
    sw.print("M4P4C1C2C5C8");
    sw.println();
    delay(4000);
    sw.print("M5P4C1C2C5C8");
    sw.println();
    delay(2000);
    sw.print("M6P4C1C2C5C8");
    sw.println();
    delay(2000);
    j = '0';
  }
}
