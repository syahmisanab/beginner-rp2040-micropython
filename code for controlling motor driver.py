# Import the necessary library for the LCD screen
#include <LiquidCrystal.h>

// Motor A connections
int enA = 9;
int in1 = 8;
int in2 = 7;
// Motor B connections
int enB = 3;
int in3 = 5;
int in4 = 4;
// Buttons
int buttonA = 2;
int buttonB = 6;
int buttonC = 10;  // Third button for increasing Motor A speed
int buttonD = 11;  // Fourth button for increasing Motor B speed

// LCD screen connections
LiquidCrystal lcd(12, 13, 14, 15, 16, 17);

void setup() {
  // Set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  // Set button pins to inputs
  pinMode(buttonA, INPUT_PULLUP);
  pinMode(buttonB, INPUT_PULLUP);
  pinMode(buttonC, INPUT_PULLUP);
  pinMode(buttonD, INPUT_PULLUP);

  // Initialize the LCD screen
  lcd.begin(16, 2);
  lcd.print("Motor Speed:");

  // Turn off motors - Initial state
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}

void loop() {
  if (digitalRead(buttonA) == LOW) {
    controlMotorA();
  }
  if (digitalRead(buttonB) == LOW) {
    controlMotorB();
  }
  if (digitalRead(buttonC) == LOW) {
    increaseMotorASpeed();
  }
  if (digitalRead(buttonD) == LOW) {
    increaseMotorBSpeed();
  }
  speedControl();
  displaySpeed();
  delay(100);
}

// This function controls Motor A
void controlMotorA() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
}

// This function controls Motor B
void controlMotorB() {
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
}

// This function increases the speed of Motor A
void increaseMotorASpeed() {
  int currentSpeed = analogRead(enA);  // Read the current speed
  int newSpeed = currentSpeed + 10;  // Increase the speed by 10 (you can adjust this value)
  if (newSpeed > 255) {
    newSpeed = 255;  // Ensure the speed does not exceed the maximum value
  }
  analogWrite(enA, newSpeed);  // Set the new speed
}

// This function increases the speed of Motor B
void increaseMotorBSpeed() {
  int currentSpeed = analogRead(enB);  // Read the current speed
  int newSpeed = currentSpeed + 10;  // Increase the speed by 10 (you can adjust this value)
  if (newSpeed > 255) {
    newSpeed = 255;  // Ensure the speed does not exceed the maximum value
  }
  analogWrite(enB, newSpeed);  // Set the new speed
}

// This function lets you control speed of the motors
void speedControl() {
  // Read the analog value from a potentiometer connected to A0 pin
  int potValue = analogRead(A0);

  // Map the potentiometer value to the PWM range
  int speed = map(potValue, 0, 1023, 0, 255);

  // Set the motor speed
  analogWrite(enA, speed);
  analogWrite(enB, speed);

  // Turn off motors if all buttons are released
  if (digitalRead(buttonA) == HIGH && digitalRead(buttonB) == HIGH && digitalRead(buttonC) == HIGH && digitalRead(buttonD) == HIGH) {
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
    digitalWrite(in3, LOW);
    digitalWrite(in4, LOW);
  }
}
