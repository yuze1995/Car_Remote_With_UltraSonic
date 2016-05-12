# coding=utf-8

import threading
from pack import TimeStopClass


class TimeStopThread(threading.Thread):
    def __init__(self, trigger_pin, echo_pin, car):
        threading.Thread.__init__(self)
        self.TimeStopController = TimeStopClass.TimeStop(trigger_pin, echo_pin, car)

    def run(self):
        self.TimeStopController.start()
