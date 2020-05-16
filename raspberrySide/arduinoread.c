#include <Servo.h>

Servo servoTilt;
Servo servoPan;

int servoIndex; //0 = tilt / 1 = pan
int BIT_RATE = 9600;
int SERVO_DELAY = 15;
int counter = 0;
int ARDUINO_TILT_PIN = 9;
int ARDUINO_PAN_PIN = 7;
int tiltValue;
int panValue;
int lastTilt = 0;
int lastPan = 0;

String readString;
String positionString;

char readChar;
char carray1[6]; //magic needed to convert string to a number

void setup()
{
  servoTilt.attach(ARDUINO_TILT_PIN);
  servoPan.attach(ARDUINO_PAN_PIN);
  Serial.begin(BIT_RATE);
}

void loop()
{
  if (Serial.available())
  { //From RPi to Arduino
    if (Serial.available() > 0)
    {
      readChar = Serial.read(); //gets one byte from serial buffer
      readString += readChar;   //append the char to the string
      counter++;                //length(readString)
      Serial.println(counter);
    }
    if (readString.length() > 0)
    {
      Serial.println(readString);
    }
    if (counter == 5)
    { //at this position we are expecting either a t or p
      if (readChar == 't')
        servoIndex = 0;
      else if (readChar == 'p')
        servoIndex = 1;
    }

    if (counter == 6)
    {
      positionString = readString.substring(1, 4); //get the angle value in range(0-180)
      Serial.println(positionString);
      readString = "";
      positionString.toCharArray(carray1, sizeof(carray1));
      if (servoIndex == 0)
      {
        tiltValue = atoi(carray1);
      }
      else if (servoIndex == 1)
      {
        panValue = atoi(carray1); //string to int
      }
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
  delay(SERVO_DELAY); // waits for the servo to get there
}
