from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

hub = MSHub()
movement_motors = MotorPair('B', 'A')
color_sensor = ColorSensor('E')


hub.speaker.beep()

def pathfinder()
while True:
    movement_motors.start((color_sensor.get_reflected_light()-50)*3, 11)
