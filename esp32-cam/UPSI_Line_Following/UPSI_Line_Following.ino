/*
///////////////////////////////////////////////////////////////////////////////
        * Created by Bizbot Technology
        *
        * This is example code for UPSi student
        *
        * Visit our wibsite for any inquiry: https://www.bveetamini.com/
        *
        * Follow our social media to know our latest update
           * 
           * https://whatsapp.com/channel/0029Va6H23XCXC3MqHMSe61L
           *
           * https://www.linkedin.com/company/bizbot-technology/
           *
 /////////////////////////////////////////////////////////////////////////////
*/

//Right Motor A Pin connections
int enA = 12;
int in1 = 13;
int in2 = 15;
// Motor B Pin connections
int enB = 16;
int in3 = 14;
int in4 = 2;

//Pin sensor connection
const int irSensorPin = 0; //right
const int irSensorPin2 = 4; //LEFT

//constant variable
int rightstate = LOW;
int leftstate = LOW;

void setup() {
	// Set all the motor control and ir pins to outputs or input
  Serial.begin(115200) ;
	pinMode(enA, OUTPUT);
	pinMode(enB, OUTPUT);
	pinMode(in1, OUTPUT);
	pinMode(in2, OUTPUT);
	pinMode(in3, OUTPUT);
	pinMode(in4, OUTPUT);

  pinMode(irSensorPin, INPUT);
  pinMode(irSensorPin2, INPUT);
	

}

void loop() {
  //read signal data from irsensor
  int sensorState = digitalRead(irSensorPin);
  int sensorState2 = digitalRead(irSensorPin2);

//one ir sensor
  // if (sensorState == HIGH){
  //   Serial.println("black route");
  //   delay(300);
  //   right();
  //   delay(500);
  // }

  // else if (sensorState == LOW){
  //   Serial.println("white route");
  //   forward();
  // }

//Two IR Sensor
  if (sensorState == HIGH && sensorState2 == LOW && rightstate == LOW){
    Serial.println("turn right");
    rightstate = !rightstate;
    // delay(100);
    right();
    delay(500);
  }

  else if(sensorState == LOW && sensorState2 == HIGH && leftstate == LOW){
    Serial.println("turn left");
    leftstate = !leftstate;
    // delay(100);
    left();
    delay(500);
  }

  else if (sensorState == LOW && sensorState2 == LOW){
    Serial.println("white route");
    rightstate = LOW;
    leftstate = LOW;
    forward();
  }

}





void forward(void) {
  // For PWM maximum possible values are 0 to 255
	analogWrite(enA, 180);
	analogWrite(enB, 255);

	// Turn on motor A & B
	digitalWrite(in1, LOW);
	digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
	digitalWrite(in4, HIGH);
}

void backward(void) {
	// For PWM maximum possible values are 0 to 255
	analogWrite(enA, 180);
	analogWrite(enB, 255);

	// Turn on motor A & B
	 digitalWrite(in1, HIGH);
	 digitalWrite(in2, LOW);
	digitalWrite(in3, HIGH);
	digitalWrite(in4, LOW);
}

void right(void) {
   	// For PWM maximum possible values are 0 to 255
	analogWrite(enA, 180);
	analogWrite(enB, 180);

	// Turn on motor A & B
	digitalWrite(in1, HIGH);
	digitalWrite(in2, LOW);
	digitalWrite(in3, LOW);
	digitalWrite(in4, HIGH);
}
void left(void) {
 	// For PWM maximum possible values are 0 to 255
	analogWrite(enA, 180);
	analogWrite(enB, 180);

	// Turn on motor A & B
	digitalWrite(in1, LOW);
	digitalWrite(in2, HIGH);
	digitalWrite(in3, HIGH);
	digitalWrite(in4, LOW);
}


void stopped(void) {
      	// For PWM maximum possible values are 0 to 255
	analogWrite(enA, 0);
	analogWrite(enB, 0);

	// Turn on motor A & B
	digitalWrite(in1, HIGH);
	digitalWrite(in2, LOW);
	digitalWrite(in3, HIGH);
	digitalWrite(in4, LOW);
} 

