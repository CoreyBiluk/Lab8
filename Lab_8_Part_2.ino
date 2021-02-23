// Lab 8 Part 2
// Corey Biluk
// February 22, 2021

#include <Servo.h>

// Create Servo objects
Servo myservo1;
Servo myservo2;

// Set Potentiometer pins and create variables to hold each pot value
int pot1pin = A0;
int pot2pin = A1;
int val1;
int val2;

void setup() {
  
  // Attach servos to their digital pins on the Arduino
  myservo1.attach(5);
  myservo2.attach(6);
}

void loop() {
  val1 = analogRead(pot1pin);         // Read value of first potentiometer
  val2 = analogRead(pot2pin);         // Read value of second potentiometer
  val1 = map(val1, 0, 1023, 0, 180);  // Scale value of first pot(pot value 0 - 1023 scaled to servo degrees 0 - 180)
  val2 = map(val2, 0, 1023, 0, 180);  // Scale value of second pot (pot value 0 - 1023 scaled to servo degrees 0 - 180)
  myservo1.write(val1);               // Sets servo 1 to angle value (scaled from pot value) 
  myservo2.write(val2);               // Sets servo 2 to angle value (scaled from pot value)
  delay(15);                          // wait for servo to move 
}
