#include <Servo.h>

Servo servoTilt; 
Servo servoPan; 

char dataType; //'t', 'p', 'w', 's'

const int BIT_RATE =  9600;
const int SERVO_DELAY = 35;
int counter = 0; //to decode the bytes per position

int tiltValue, panValue, powerValue;
const int PAN_PIN = 7;
const int TILT_PIN = 9;
//const int pwrInputLow = 11;
//const int pwrInputHigh = 10;
const int FORWARD_PIN = 6;
const int BACKWARD_PIN = 5;


String incomingData;
String positionString;
char readChar;
char carray1[6]; //magic needed to convert string to a number 

void setup() {
  servoTilt.attach(TILT_PIN);  
  servoPan.attach(PAN_PIN);
  //pinMode(dcInputLow, OUTPUT); 
  //pinMode(dcInputHigh, OUTPUT);  
  pinMode(FORWARD_PIN, OUTPUT);
  pinMode(BACKWARD_PIN, OUTPUT);
  Serial.begin(BIT_RATE);

}

void loop() {


  if(Serial.available()){         //From RPi to Arduino
    
    if(Serial.available() > 0){
      readChar = Serial.read();  //gets one byte from serial buffer
      incomingData += readChar; //makes the string incomingData
      
      counter ++;
      //Serial.println(counter);
    }
    if(incomingData.length() > 0){
      //Serial.println(incomingData);
    }
    if(counter == 5) dataType = readChar;
       
    if(counter == 6){
      positionString = incomingData.substring(1,4);
      //Serial.println(positionString);
      incomingData = "";
      positionString.toCharArray(carray1, sizeof(carray1));
      if(dataType == 't'){
        tiltValue = atoi(carray1); 
        servoTilt.write(tiltValue); // sets the servo position according to the scaled value
      }
      else if(dataType == 'p'){
        panValue = atoi(carray1);
          servoPan.write(panValue);
      }else if(dataType == 'w'){
        powerValue = atoi(carray1);
        analogWrite(BACKWARD_PIN, 0);
        analogWrite(FORWARD_PIN,  powerValue);   //powerValue
      }else if(dataType == 's'){
        powerValue = atoi(carray1);
        analogWrite(FORWARD_PIN, 0);
        analogWrite(BACKWARD_PIN, powerValue);
      }
      
      counter = 0;
    }
}
  //digitalWrite(dcInputLow, LOW);
  //digitalWrite(dcInputHigh,  HIGH);  
  printSerial();
  delay(SERVO_DELAY);                           // waits for the servo to get there

}


void printSerial(){
  Serial.print("---- tilt: ");
  Serial.println(tiltValue);
  Serial.print("---- pan: ");
  Serial.print(panValue);
  Serial.println("---- power: ");
  Serial.print(powerValue);
}