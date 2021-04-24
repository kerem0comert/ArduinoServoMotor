#include <Servo.h>

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
char readChar;
char intValue[6]; //magic needed to convert string to a number 
boolean seenFirstQuote = false;

void setup() {
  servoTilt.attach(TILT_PIN);  
  servoPan.attach(PAN_PIN); 
  pinMode(FORWARD_PIN, OUTPUT);
  pinMode(BACKWARD_PIN, OUTPUT);
  Serial.begin(BIT_RATE);

}

void loop() {
  if(Serial.available()){ 
      readChar = Serial.read();    //From RPi to Arduino
      Serial.println("read: " + readChar);
       incomingData += readChar;
      if(incomingData.length() == 6) {
        operateOnData();
        incomingData = "";
    }
  }
}

void operateOnData(){
  String incomingValue = incomingData.substring(1,4);
  char incomingType = incomingData[4];
  Serial.println("Position value: " + incomingValue + " Data type: " + incomingType);
  incomingValue.toCharArray(intValue, sizeof(intValue));
  if(incomingType == 't'){
    tiltValue = atoi(intValue); 
    servoTilt.write(tiltValue); // sets the servo position according to the scaled value
  }else if(incomingType == 'p'){
    panValue = atoi(intValue);
    servoPan.write(panValue);
  }else if(incomingType == 'w'){
    powerValue = atoi(intValue);
    analogWrite(BACKWARD_PIN, 0);
    analogWrite(FORWARD_PIN,  powerValue);   //powerValue
  }else if(incomingType == 's'){
    powerValue = atoi(intValue);
    analogWrite(FORWARD_PIN, 0);
    analogWrite(BACKWARD_PIN, powerValue);
  }
}


void printSerial(){
 /* Serial.print("---- tilt: ");
  Serial.println(tiltValue);
  Serial.print("---- pan: ");
  Serial.print(panValue);*/
  Serial.println("---- power: ");
  Serial.print(powerValue);
}