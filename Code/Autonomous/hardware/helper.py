import RPi.GPIO as GPIO


GPIO_4 = 4


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_4, GPIO.OUT)
    GPIO.output(GPIO_4, False)