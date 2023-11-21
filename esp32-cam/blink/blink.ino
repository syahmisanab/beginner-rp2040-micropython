int led = 4;

void setup() {
	// Set all the motor control and ir pins to outputs or input
  Serial.begin(115200) ;
	pinMode(led, OUTPUT);

  }

  void loop(){

	digitalWrite(led, LOW);
  delay(500);
	digitalWrite(led, LOW);

  }