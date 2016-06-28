#include <Servo.h>

Servo myservo00;
//Servo myservo01;
//Servo myservo02;
//Servo myservo03;
//Servo myservo04;
//Servo myservo05;
//Servo myservo06;
//Servo myservo07;
//Servo myservo08;
//Servo myservo09;
//Servo myservo10;
//Servo myservo11;
//Servo myservo12;

int incomingByte = 0;   // for incoming serial data
int pos = 0;    // variable to store the servo position

void setup() {
  Serial.begin(9600);
  Serial.println("Ready to go!");
  myservo00.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  // the value in incominByte should be an ASCii conversion to Decimal numbers.
  //Use https://www.branah.com/ascii-converter for easy conversions

  if (Serial.available() != 0) {
        incomingByte = Serial.read();
        if (incomingByte == 49) { 
          servoSweep();
        }
        else if (incomingByte == 50) {
          miniSweep();
        }
        else if (incomingByte == 51) {
          wildThing();
        }
  }
}

void macroRunner(int macroNumber) {
  if (macroNumber == 0) {
    servoSweep();
  }
  else if (macroNumber == 1) {
  myservo00.write(35);
  incomingByte = 0;  
  }
}

void servoSweep() {
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo00.write(pos);              // tell servo to go to position in variable 'pos'
    delay(5);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo00.write(pos);              // tell servo to go to position in variable 'pos'
    delay(5);
  }
  incomingByte = 0;
}

void miniSweep() {
  for (pos = 30; pos <= 150; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo00.write(pos);              // tell servo to go to position in variable 'pos'
    delay(5);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 150; pos >= 30; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo00.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);
  }
  incomingByte = 0;
}

void wildThing() {
  myservo00.write(180);
  delay(150);
  myservo00.write(30);
  delay(150);
  myservo00.write(90);
  delay(150);
  myservo00.write(0);
  delay(0);
  myservo00.write(180);

}

void setAllToZero() {
  myservo00.write(0);
}

