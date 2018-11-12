/*
#****************************************************************************************************************************
#   --------------------------------------------------------------------------------------------------------------------
#   @Autecla: Testing Serial Communication with the ESP32 using Arduino IDE
#   Sketch/program to test serial communication with the ESP32 using Arduino IDE
#   In Partnership with GROOT <3
#   --------------------------------------------------------------------------------------------------------------------
#****************************************************************************************************************************
*/

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(500);// Set time out for 
}

void loop() {

   if (Serial.available()) {
     char bfr[300];
     memset(bfr,0, 301);
     Serial.readBytesUntil( '\n',bfr,300);
     Serial.print("Buffer:"); 
     Serial.println(bfr);

   }
}
