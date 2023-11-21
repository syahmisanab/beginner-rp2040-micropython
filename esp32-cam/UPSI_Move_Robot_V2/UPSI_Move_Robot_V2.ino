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
int in2 = 15
// Motor B Pin connections
int enB = 16;
int in3 = 14;
int in4 = 2;


void setup() {
	// Set all the motor control and ir pins to outputs or input
  Serial.begin(115200) ;
	pinMode(enA, OUTPUT)
	pinMode(enB, OUTPUT);
	pinMode(in1, OUTPUT);
	pinMode(in2, OUTPUT);
	pinMode(in3, OUTPUT);
	pinMode(in4, OUTPUT);

}

void loop() {

  forward();
	/*
  stopped()
  Backward();
  stopped()
  right();
  stopped()
  left();
  stopped()
*/

}

void forward() {
  // For PWM maximum possible values are 0 to 255
	analogWrite(enA, 180);
	analogWrite(enB, 255);

	// Turn on motor A & B
	digitalWrite(in1, LOW);
	digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
	digitalWrite(in4, HIGH);
}



