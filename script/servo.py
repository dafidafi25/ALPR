import RPi.GPIO as GPIO
import time

def main():
  GPIO.setmode(GPIO.BOARD)

  GPIO.setup(11,GPIO.OUT)

  p = GPIO.PWM(11, 50) # GPIO 17 for PWM with 50Hz
  p.start(2.5) # Initialization
  try:
    while True:
      p.ChangeDutyCycle(5)
      time.sleep(0.5)
      p.ChangeDutyCycle(7.5)
      time.sleep(0.5)
      p.ChangeDutyCycle(10)
      time.sleep(0.5)
      p.ChangeDutyCycle(12.5)
      time.sleep(0.5)
      p.ChangeDutyCycle(10)
      time.sleep(0.5)
      p.ChangeDutyCycle(7.5)
      time.sleep(0.5)
      p.ChangeDutyCycle(5)
      time.sleep(0.5)
      p.ChangeDutyCycle(2.5)
      time.sleep(0.5)
  except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()


class GateServo:
  def __init__(self):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    self.servo = GPIO.PWM(11,50)
    self.servo.start(0)
    time.sleep(1)
    self.duty = 0

  def open(self):
    while self.duty <= 12.5:
      self.servo.ChangeDutyCycle(self.duty)
      time.sleep(0.05)
      self.duty = self.duty + 2.5

  def close(self):
    while self.duty >= 2.5:
      self.servo.ChangeDutyCycle(self.duty)
      time.sleep(0.05)
      self.duty = self.duty - 2.5


if __name__ == '__main__':
  Servo = GateServo()
  Servo.open()
  Servo.close ()


