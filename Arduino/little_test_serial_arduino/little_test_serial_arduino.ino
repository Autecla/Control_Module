#include <SoftwareSerial.h>

SoftwareSerial sw(2, 3); // RX, TX

void setup() {
  Serial.begin(9600);
  sw.begin(9600);
}

void loop() {
  Serial.println("enviando");
  sw.println("test...");
  delay(1000);
}
