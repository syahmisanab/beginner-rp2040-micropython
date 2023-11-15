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

//Right Motor A connections
int enA = 12;
int in1 = 13;
int in2 = 15;
// Motor B connections
int enB = 16;
int in3 = 14;
int in4 = 2;

//Ultrasonic sensor pins 1
// int trigPin1 = 5;
// int echoPin1 = 6;

//constant variable
// long duration1;
// long distance1;

//Ultrasonic sensor pins 2
int trigPin2 = 3;
int echoPin2 = 0;

//constant variable
long duration2;
long distance2;

//Ultrasonic sensor pins 3
// int trigPin3 = 12;
// int echoPin3 = 13;

//constant variable
// long duration3;
// long distance3;

void setup() {
	// Set all the motor control pins and ultrasonic to outputs or input
  Serial.begin(115200) ;

	pinMode(enA, OUTPUT);
	pinMode(enB, OUTPUT);
	pinMode(in1, OUTPUT);
	pinMode(in2, OUTPUT);
	pinMode(in3, OUTPUT);
	pinMode(in4, OUTPUT);

  // pinMode(trigPin1, OUTPUT);
  // pinMode(echoPin1, INPUT);

  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);

  // pinMode(trigPin3, OUTPUT);
  // pinMode(echoPin3, INPUT);
	

}

// //Void function for right ultrasonic sensor measurement calculations
// void sendSensor1(void)
// {
  
//    //clear the trigPin
//   digitalWrite(trigPin1, LOW);
//   delayMicroseconds(2);
  
//   //Set the trigPin on HIGH state for 10 micro seconds
//   digitalWrite(trigPin1, HIGH);
//   delayMicroseconds(10);
//   digitalWrite(trigPin1, LOW);
  
//   //Read the echoPin, return to sound wave travel time to microseconds
//   duration1 = pulseIn(echoPin1, HIGH);
  
//   //Calculating the distance
//   distance1 = (duration1*0.034/2); //s=t*v
//   Serial.print("distance1:");
//   Serial.println(distance1);
//   // delay(500);


// }

//Void function for middle ultrasonic sensor measurement calculations
void sendSensor2(void)
{
  
   //clear the trigPin
  digitalWrite(trigPin2, LOW);
  delayMicroseconds(2);
  
  //Set the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);
  
  //Read the echoPin, return to sound wave travel time to microseconds
  duration2 = pulseIn(echoPin2, HIGH);
  
  //Calculating the distance
  distance2 = (duration2*0.034/2); //s=t*v
  Serial.print("distance2:");
  Serial.println(distance2);
  // delay(500);


}

//Void function for left ultrasonic sensor measurement calculations
// void sendSensor3(void)
// {
  
//    //clear the trigPin
//   digitalWrite(trigPin3, LOW);
//   delayMicroseconds(2);
  
//   //Set the trigPin on HIGH state for 10 micro seconds
//   digitalWrite(trigPin3, HIGH);
//   delayMicroseconds(10);
//   digitalWrite(trigPin3, LOW);
  
//   //Read the echoPin, return to sound wave travel time to microseconds
//   duration3 = pulseIn(echoPin3, HIGH);
  
//   //Calculating the distance
//   distance3 = (duration3*0.034/2); //s=t*v
//   Serial.print("distance3:");
//   Serial.println(distance3);
//   // delay(500);


// }


void loop() {
  // sendSensor1();
  sendSensor2();
  // sendSensor3();

//one ultrasonics
  if (distance2 > 40){
      forward();
      Serial.println("Forward");
    }

  else {
    Serial.println("backward");
    backward();
    delay(300);
    left();
    delay(300);
  }

//three ultrasonics
  // if (distance2 > 40){
  //   //right
  //   if (distance1 <= 15){
  //     Serial.println("go left");
  //     left();
  //     delay(500);
  //   }

  //   else if (distance3 <= 15){
  //     Serial.println("go right");
  //     right();
  //     delay(500);

  //   }

  //   else {
  //     forward();
  //     Serial.println("Forward");
  //   }
  // }
  // else if (distance2 < 40){
  //   Serial.println("backward");
  //   backward();
  //   delay(300);
  //   left();
  //   delay(300);
  // }


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

