# coding=utf-8

import threading
from pack import CarControlClass


class CarControlThread(threading.Thread):
    def __init__(self, left1_pin, left2_pin, right1_pin, right2_pin):
        threading.Thread.__init__(self)
        self.carController = CarControlClass.CarControl(left1_pin, left2_pin, right1_pin, right2_pin)

    def run(self):
        self.carController.start()

    def stopRunning(self):
        self.carController.stop()

    def setDirection(self, direction):
        self.carController.status = direction

    def startRunning(self):
        self.carController.start()
