int buttonState = 0;

void setup()
{
  pinMode(2, INPUT);
  pinMode(13, OUTPUT);
}

void loop()
{
  // Initialize button state with LOW or 0
  buttonState = 0;
  // Read State of Pin number 2
  buttonState = digitalRead(2);
  if (buttonState == 1) {
    digitalWrite(13, HIGH);
    delay(1000); // Wait for 1000 millisecond(s)
  } else {
    digitalWrite(13, LOW);
  }
}
