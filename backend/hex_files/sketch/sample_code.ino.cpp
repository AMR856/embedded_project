#include <Arduino.h>
#line 1 "H:\\embedded_project\\backend\\sample_code\\sample_code.ino"
#line 1 "H:\\embedded_project\\backend\\sample_code\\sample_code.ino"
void setup();
#line 6 "H:\\embedded_project\\backend\\sample_code\\sample_code.ino"
void loop();
#line 1 "H:\\embedded_project\\backend\\sample_code\\sample_code.ino"
void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
