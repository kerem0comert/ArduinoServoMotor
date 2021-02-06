
#include <Servo.h>

Servo servoTilt; 
Servo servoPan; 

int dataType; //0 = tilt / 1 = pan / 2 = power


const int bitRate =  9600;
const int servoDelay = 35;
int counter = 0; //to decode the bytes per position

int tiltValue, panValue, powerValue, potentValue;
const int panPin = 7;
const int tiltPin = 9;
const int dcInputLow = 11;
const int dcInputHigh = 10;
const int dcEnable = 6;
const int potentPin = A0;

int lastTilt = 0;
int lastPan = 0;
int lastPower = 0;



String incomingData;
String positionString;
char readChar;
char carray1[6]; //magic needed to convert string to a number 

void setup() {
  servoTilt.attach(tiltPin);  
  servoPan.attach(panPin);
  pinMode(dcInputLow, OUTPUT); 
  pinMode(dcInputHigh, OUTPUT);  
  pinMode(dcEnable, OUTPUT);
  Serial.begin(bitRate);

}

void loop() {


  if(Serial.available()){         //From RPi to Arduino
    
    if(Serial.available() > 0){
      readChar = Serial.read();  //gets one byte from serial buffer
      incomingData += readChar; //makes the string incomingData
      
      counter ++;
      //Serial.println(counter);
    }
    /*if(incomingData.length() > 0){
      Serial.println(incomingData);
    }*/
    if(counter == 5){
      if(readChar == 't')
      {
        //Serial.print("t found");
        dataType = 0;
      }else if(readChar == 'p')
      {
        //Serial.print("p found");
        dataType = 1;
      }else if(readChar == 'w')
      {
        //Serial.print("w found");
        dataType = 2;
      }
       }

    if(counter == 6){
      positionString = incomingData.substring(1,4);
      //Serial.println(positionString);
      incomingData = "";
      positionString.toCharArray(carray1, sizeof(carray1));
      if(dataType == 0){
        tiltValue = atoi(carray1); 
      }
      else if(dataType == 1){
        panValue = atoi(carray1);
      }else if(dataType == 2){
        powerValue = atoi(carray1);
      }
      //Serial.print("tilt");
      //Serial.println(tiltValue);
      counter = 0;
    }
}


  servoTilt.write(lastTilt + tiltValue); // sets the servo position according to the scaled value
  lastTilt = tiltValue;
  servoPan.write(lastPan + panValue);
  analogWrite(dcEnable,  powerValue);   //powerValue
  digitalWrite(dcInputLow, LOW);
  digitalWrite(dcInputHigh,  HIGH);  
  lastPan = panValue;  
  lastPower = powerValue;
  /*Serial.print("---- tilt: ");
  Serial.println(lastTilt + tiltValue);
  Serial.print("---- pan: ");
  Serial.print(lastPan + panValue);
  Serial.print("---- power: ");
  Serial.print(powerValue);
  Serial.print("---potent: "); */
  potentValue = analogRead(potentPin);
  Serial.println(potentValue);
  /*Serial.flush();
  Serial.print(potentValue);  */
  delay(servoDelay);                           // waits for the servo to get there

}
