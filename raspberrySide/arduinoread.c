#include <Servo.h>

Servo servoTilt;  

int incomingData = 1;
int bitRate =  9600;
int servoDelay = 15;

int tiltPin = 9;
int tiltValue;   

void setup() {
  servoTilt.attach(tiltPin);  
  Serial.begin(bitRate);

}

void loop() {


  if(Serial.available()){         //From RPi to Arduino
    incomingData = (incomingData * (Serial.read() - '0')) + 48; 
    Serial.println(incomingData);
    tiltValue = incomingData;
    incomingData = 1; //reset the coefficent for conversion
  }

  servoTilt.write(tiltValue);                  // sets the servo position according to the scaled value
  Serial.print("---- tilt: ");
  Serial.println(tiltValue);
  delay(servoDelay);                           // waits for the servo to get there

}
