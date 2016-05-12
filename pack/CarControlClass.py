# coding=utf-8

from pack import CarMoveClass


class CarControl():
    def __init__(self, left1_pin, left2_pin, right1_pin, right2_pin):
        """
        0 => stop
        1 => forward
        2 => back
        3 => left
        4 => right
        """
        self.status = 0
        self.isStop = True
        self.car_move = CarMoveClass.CarDirect(left1_pin, left2_pin, right1_pin, right2_pin)

    def start(self):
        while True:
            if self.isStop == False:
                if self.status == 0:
                    self.car_move.stop()
                    self.isStop = True
                elif self.status == 1:
                    self.car_move.forward()
                    self.isStop = True
                elif self.status == 2:
                    self.car_move.back()
                    self.isStop = True
                elif self.status == 3:
                    self.car_move.left()
                    self.isStop = True
                elif self.status == 4:
                    self.car_move.right()
                    self.isStop = True
