# coding=utf-8

import threading
from pack import UltraSonicDetectClass


class TimeStop():
    def __init__(self, trigger_pin, echo_pin, car):
        self.isTimerStop = True  # 判斷Timer是否結束,True => 停止 , False => 使用中
        self.isStartDetect = False  # 判斷是否要進行超聲波偵測
        self.timer = None
        self.car = car
        self.second = 0
        self.direction = 0
        self.ultra_sonic = UltraSonicDetectClass.UltraSonicDetect(trigger_pin, echo_pin)

    def start(self):
        while True:
            if self.isStartDetect == True:
                self.timer = threading.Timer(self.second, self.stop)
                self.timer.start()

                self.isTimerStop = False
                self.isStartDetect = False

                self.car.status = self.direction
                self.car.isStop = False

                while True:
                    if self.isTimerStop == True:
                        self.stop()
                        break
                    else:
                        if self.ultra_sonic.detect() == False:
                            self.stop()
                            break

    def stop(self):
        self.car.car_move.stop()
        self.timer.cancel()
        self.isTimerStop = True
        self.isStartDetect = False
        self.car.status = 0
        self.car.isStop = True
        self.second = 0
        self.direction = 0

    def timerStart(self, second, direction):
        self.second = second
        self.direction = direction
        self.isStartDetect = True
