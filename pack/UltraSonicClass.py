# coding=utf-8

import RPi.GPIO as GPIO
import time

global car


class UltraSonic():
    def __init__(self, trig, echo):
        self.trig_pin = trig
        self.echo_pin = echo
        self.setup()

    def setup(self):
        # set pin
        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def get_cm(self, second):
        GPIO.output(self.trig_pin, True)
        time.sleep(second)
        GPIO.output(self.trig_pin, False)

        while GPIO.input(self.echo_pin) == False:
            pass
        start = time.time()

        while GPIO.input(self.echo_pin) == True:
            pass
        end = time.time()

        return ((end - start) * 340 * 100 / 2)  # time_length = end - start
