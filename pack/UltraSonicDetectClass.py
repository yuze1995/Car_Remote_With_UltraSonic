from pack import UltraSonicClass


class UltraSonicDetect():
    def __init__(self, trigger_pin, echo_pin):
        self.second = 0
        self.ultra_sonic_detect = UltraSonicClass.UltraSonic(trigger_pin, echo_pin)

    def detect(self):
        while True:
            if self.ultra_sonic_detect.get_cm(self.second) <= 20:
                # print("false")
                return False
            else:
                # print("true")
                return True
