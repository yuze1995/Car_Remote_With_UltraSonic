# coding=utf-8

import RPi.GPIO as GPIO
import time


class CarDirect():
    """docstring for ClassName"""

    def __init__(self, left_1, left_2, right_1, right_2):
        self.left1_pin = left_1
        self.left2_pin = left_2

        self.right1_pin = right_1
        self.right2_pin = right_2

        self.setup()

    def setup(self):
        # left wheel
        GPIO.setup(self.left1_pin, GPIO.OUT)
        GPIO.setup(self.left2_pin, GPIO.OUT)
        # right wheel
        GPIO.setup(self.right1_pin, GPIO.OUT)
        GPIO.setup(self.right2_pin, GPIO.OUT)

    def forward(self):
        GPIO.output(self.left1_pin, GPIO.HIGH)
        GPIO.output(self.left2_pin, GPIO.LOW)
        GPIO.output(self.right1_pin, GPIO.HIGH)
        GPIO.output(self.right2_pin, GPIO.LOW)

    def back(self):
        GPIO.output(self.left1_pin, GPIO.LOW)
        GPIO.output(self.left2_pin, GPIO.HIGH)
        GPIO.output(self.right1_pin, GPIO.LOW)
        GPIO.output(self.right2_pin, GPIO.HIGH)

    def left(self):
        GPIO.output(self.left1_pin, GPIO.HIGH)
        GPIO.output(self.left2_pin, GPIO.LOW)
        GPIO.output(self.right1_pin, GPIO.LOW)
        GPIO.output(self.right2_pin, GPIO.HIGH)

    def right(self):
        GPIO.output(self.left1_pin, GPIO.LOW)
        GPIO.output(self.left2_pin, GPIO.HIGH)
        GPIO.output(self.right1_pin, GPIO.HIGH)
        GPIO.output(self.right2_pin, GPIO.LOW)

    def stop(self):
        GPIO.output(self.left1_pin, GPIO.LOW)
        GPIO.output(self.left2_pin, GPIO.LOW)
        GPIO.output(self.right1_pin, GPIO.LOW)
        GPIO.output(self.right2_pin, GPIO.LOW)
