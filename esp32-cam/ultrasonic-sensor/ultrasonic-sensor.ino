// Define the pins for the ultrasonic sensor
const int trigPin = 13;
const int echoPin = 14;

// Define variables for the duration and the distance
long duration;
int distance;

void setup() {
  // Begin serial communication at a baud rate of 9600
  
  // Define pin modes
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // Clear the trigPin by setting it LOW
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Trigger the sensor by setting the trigPin high for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);

  // Calculate the distance
  distance= duration*0.034/2;

  // Print the distance on the Serial Monitor
  Serial.print("Distance: ");
  Serial.println(distance);

  // Delay 50ms before the next measurement
  delay(50);
}
