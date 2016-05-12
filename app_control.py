# coding=utf-8

import RPi.GPIO as GPIO
import decimal
# from pack import UltraSonicDetectClass  # , ThreadClass, CarControlClass, TimeStopClass,
from Thread import CarControlThreadClass, TimeStopThreadClass
from flask import Flask, render_template, request

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

left1_pin = 22
left2_pin = 23
right1_pin = 24
right2_pin = 26

trigger_pin = 3  # output
echo_pin = 5  # input

# car = CarControlClass.CarControl(left1_pin, left2_pin, right1_pin, right2_pin)
# ultra_sonic = UltraSonicDetectClass.UltraSonicDetect(trigger_pin, echo_pin)
# time_stop = TimeStopClass.TimeStop()
carThread = CarControlThreadClass.CarControlThread(left1_pin, left2_pin, right1_pin, right2_pin)
timeStopThread = TimeStopThreadClass.TimeStopThread(trigger_pin, echo_pin, carThread.carController)

app = Flask(__name__)


@app.route('/')
def index():
    carThread.start()
    timeStopThread.start()
    return render_template('index.html')


# forward
@app.route('/forward', methods=['GET'])
def forward():
    length = decimal.Decimal(request.args.get('length'))
    control(length, 1)
    return 'True'


# back
@app.route("/back", methods=['GET'])
def back():
    length = decimal.Decimal(request.args.get('length'))
    control(length, 2)
    return 'True'


# left
@app.route("/left", methods=['GET'])
def left():
    length = decimal.Decimal(request.args.get('length'))
    control(length, 3)
    return 'True'


# right
@app.route("/right", methods=['GET'])
def right():
    length = decimal.Decimal(request.args.get('length'))
    control(length, 4)
    return 'True'


# stop
@app.route("/stop", methods=['GET'])
def stop():
    timeStopThread.TimeStopController.stop()
    return 'True'


def control(second, direction):
    timeStopThread.TimeStopController.timerStart(second, direction)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
