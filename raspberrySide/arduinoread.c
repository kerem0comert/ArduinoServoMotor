#include <Servo.h>
#include <ctype.h>

Servo servoTilt; 
Servo servoPan; 

char dataType; //'t', 'p', 'w', 's'

const int BIT_RATE =  9600;
const int SERVO_DELAY = 24;
int counter = 0; //to decode the bytes per position

int tiltValue, panValue, powerValue;
const int PAN_PIN = 7;
const int TILT_PIN = 9;
const int FORWARD_PIN = 6;
const int BACKWARD_PIN = 5;
const int POTENT_PIN = 0;


String incomingData;
String positionString;
int potentValue;
char readChar;
char intValue[6]; //magic needed to convert string to a number 
boolean seenFirstQuote = false;

void setup() {
  servoTilt.attach(TILT_PIN);  
  servoPan.attach(PAN_PIN); 
  pinMode(FORWARD_PIN, OUTPUT);
  pinMode(BACKWARD_PIN, OUTPUT);
  Serial.begin(BIT_RATE);
  //delay(100);
}

void loop() {
  if(Serial.available()){ 
      readChar = Serial.read();    //From RPi to Arduino
      if(isAlpha(readChar)){
        operateOnData(readChar);
        incomingData = "";
      }else incomingData += readChar; 
    }
    potentValue = analogRead(POTENT_PIN);
    Serial.write(potentValue);
}

void operateOnData(char readChar){
  //String incomingValue = incomingData.substring(1,incomingData.length()-1);
  if(readChar == 't'){
    tiltValue = incomingData.toInt(); 
    servoTilt.write(tiltValue);
  }else if(readChar == 'p'){
    panValue = incomingData.toInt(); 
    servoPan.write(panValue);
  }else if(readChar == 'w'){
    powerValue = incomingData.toInt(); 
    analogWrite(BACKWARD_PIN, 0);
    analogWrite(FORWARD_PIN,  powerValue);   //powerValue
  }else if(readChar == 's'){
    powerValue = incomingData.toInt(); 
    analogWrite(FORWARD_PIN, 0);
    analogWrite(BACKWARD_PIN, powerValue);
  }
  
   //Serial.println(potentValue);
   //printSerial();
}


void printSerial(){
  Serial.print("---- tilt: ");
  Serial.println(tiltValue);
  Serial.println("---- pan: ");
  Serial.print(panValue);
  Serial.println("---- power: ");
  Serial.print(powerValue);
}