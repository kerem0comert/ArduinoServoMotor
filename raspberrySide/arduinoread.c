
#include <Servo.h>

Servo servoTilt; 
Servo servoPan; 

int dataType; //0 = tilt / 1 = pan / 2 = power

int incomingData = 1;
int bitRate =  9600;
int servoDelay = 15;
int counter = 0;

int tiltPin = 9;
int tiltValue;   

int panPin = 7;
int panValue;

int powerPin = 8;
int powerValue;

int lastTilt = 0;
int lastPan = 0;
int lastPower = 0;


String readString;
String positionString;
char readChar;
char carray1[6]; //magic needed to convert string to a number 

void setup() {
  servoTilt.attach(tiltPin);  
  servoPan.attach(panPin);
  Serial.begin(bitRate);

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
        dataType = 0;
      }else if(readChar == 'p')
      {
        Serial.print("p found");
        dataType = 1;
      }else if(readChar == 'w')
      {
        Serial.print("w found");
        dataType = 2;
      }
       }

    if(counter == 6){
      positionString = readString.substring(1,4);
      Serial.println(positionString);
      readString = "";
      positionString.toCharArray(carray1, sizeof(carray1));
      if(dataType == 0){
        tiltValue = atoi(carray1); 
      }
      else if(dataType == 1){
        panValue = atoi(carray1);
      }else if(dataType == 2){
        powerValue = atoi(carray1);
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
  lastPower = powerValue;
  Serial.print("---- tilt: ");
  Serial.println(lastTilt + tiltValue);
  Serial.print("---- pan: ");
  Serial.print(lastPan + panValue);
  Serial.print("---- power: ");
  Serial.print(lastPower + powerValue);
  delay(servoDelay);                           // waits for the servo to get there

}
