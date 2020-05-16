
#include <Servo.h>

Servo servoTilt; 
Servo servoPan; 

int servoIndex; //0 = tilt / 1 = pan

int incomingData = 1;
int BIT_RATE =  9600;
int servoDelay = 15;
int counter = 0;

int ARD_TILT_PIN = 9;
int tiltValue;   

int ARD_PAN_PIN = 7;
int panValue;

int lastTilt = 0;
int lastPan = 0;


String readString;
String positionString;
char readChar;
char carray1[6]; //magic needed to convert string to a number 

void setup() {
  servoTilt.attach(ARD_TILT_PIN);  
  servoPan.attach(ARD_PAN_PIN);
  Serial.begin(BIT_RATE);

}

void loop() {


  if(Serial.available()){         //From RPi to Arduino
    
    if(Serial.available() > 0){
      readChar = Serial.read();  //gets one byte from serial buffer
      readString += readChar; //makes the string readString
      counter ++;
      Serial.println(counter);
    }
    if(readString.length() > 0){
      Serial.println(readString);
    }
    if(counter == 5){
      if(readChar == 't')
      {
        Serial.print("t found");
        servoIndex = 0;
      }

      else if(readChar == 'p')
      {
        Serial.print("p found");
        servoIndex = 1;
      }
       }

    if(counter == 6){
      positionString = readString.substring(1,4);
      Serial.println(positionString);
      readString = "";
      positionString.toCharArray(carray1, sizeof(carray1));
      if(servoIndex == 0){
        tiltValue = atoi(carray1); 
      }
      else if(servoIndex == 1){
        panValue = atoi(carray1);
      }
      Serial.print("tilt");
      Serial.println(tiltValue);
      counter = 0;
      }
}


  servoTilt.write(lastTilt + tiltValue); // sets the servo position according to the scaled value
  lastTilt = tiltValue;
  servoPan.write(lastPan + panValue);     
  lastPan = panValue;  
  Serial.print("---- tilt: ");
  Serial.println(lastTilt + tiltValue);
  Serial.print("---- pan: ");
  Serial.print(lastPan + panValue);
  delay(servoDelay);                           // waits for the servo to get there

}
