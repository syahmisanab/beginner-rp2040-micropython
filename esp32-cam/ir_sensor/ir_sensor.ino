// Define the IR sensor pin
int irSensorPin = 2;  // Assume the IR sensor is connected to digital pin 2

void setup() {
  Serial.begin(9600);          // Start serial communication at 9600 baud rate
  pinMode(irSensorPin, INPUT); // Set the IR sensor pin as input
}

void loop() {
  int sensorState = digitalRead(irSensorPin); // Read the sensor state

  // Check if the surface is black or white
  if (sensorState == HIGH) {
    Serial.println("White surface detected"); // HIGH usually means white surface
  } else {
    Serial.println("Black surface detected"); // LOW usually means black surface
  }

  delay(500); // Short delay before the next reading
}
