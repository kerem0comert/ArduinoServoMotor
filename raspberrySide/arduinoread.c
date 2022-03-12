#include <Servo.h>
#include <ctype.h>

Servo svTiltCamera;
Servo svPanCamera;
Servo svSteer;

const int BIT_RATE = 9600;
const int SERVO_DELAY = 24;

const int PIN_POTENT = 0;
const int PIN_POWER_BACKWARD = 5;
const int PIN_POWER_FORWARD = 6;
const int PIN_PAN_CAMERA = 7;
const int PIN_TILT_CAMERA = 8;
const int PIN_STEER = 9;

// Data types
const char STEER = 'e';
const char TILT_CAMERA = 't';
const char PAN_CAMERA = 'p';
const char POWER_FORWARD = 'w';
const char POWER_BACKWARD = 's';

int valTiltCamera, valPanCamera, valPower, valSteer, valPotent;
int counter = 0; // to decode the bytes per position
String incomingData;
String positionString;
char readChar;
char intValue[6]; // magic needed to convert string to a number
boolean seenFirstQuote = false;

char dataType; //'t', 'p', 'w', 's'

void setup()
{
  svTiltCamera.attach(PIN_TILT_CAMERA);
  svPanCamera.attach(PIN_PAN_CAMERA);
  pinMode(PIN_POWER_FORWARD, OUTPUT);
  pinMode(PIN_POWER_BACKWARD, OUTPUT);
  Serial.begin(BIT_RATE);
  // delay(100);
}

void loop()
{
  if (Serial.available())
  {
    readChar = Serial.read(); // From RPi to Arduino
    if (isAlpha(readChar))
    {
      operateOnData(readChar);
      incomingData = "";
    }
    else
      incomingData += readChar;
  }
  // delay(100);
}

void operateOnData(char readChar)
{
  int start = millis();
  // String incomingValue = incomingData.substring(1,incomingData.length()-1);
  if (readChar == TILT_CAMERA)
  {
    valTiltCamera = incomingData.toInt();
    svTiltCamera.write(valTiltCamera);
  }
  else if (readChar == PAN_CAMERA)
  {
    valPanCamera = incomingData.toInt();
    svPanCamera.write(valPanCamera);
  }
  else if (readChar == POWER_FORWARD)
  {
    valPower = incomingData.toInt();
    analogWrite(PIN_POWER_BACKWARD, 0);
    analogWrite(PIN_POWER_FORWARD, valPower); // powerValue
  }
  else if (readChar == POWER_BACKWARD)
  {
    valPower = incomingData.toInt();
    analogWrite(PIN_POWER_FORWARD, 0);
    analogWrite(PIN_POWER_BACKWARD, valPower);
  }
  else if (readChar == STEER)
  {
  }
  valPotent = analogRead(PIN_POTENT);
  Serial.println(valPotent);
  // Serial.println(potentValue);
  // printSerial();
}

void printSerial()
{
  Serial.print("---- tilt: " + valTiltCamera "\n---- pan: " + valPanCamera + "\n---- power:
    " + valPower + "\n----valSteer: " + valSteer);
}
