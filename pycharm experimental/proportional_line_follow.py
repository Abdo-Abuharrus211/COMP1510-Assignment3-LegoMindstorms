from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, \
    not_equal_to
import math
hub = MSHub()
movement_motors = MotorPair('B', 'A')
color_sensor = ColorSensor('E')


def pathfinder(target_path, prop_constant, movement_speed):
    """
    Process environmental variables and navigate the path
    :param target_path: integer value representing the color sensor's reading
    :param prop_constant: integer value representing proportional constant serving as steer sensitivity
    :param movement_speed: integer value representing motor-pair speed
    :precondition: only accept integer arguments
    :postcondition: run the robot and navigate the path accordingly
    """
    hub.speaker.beep()
    movement_motors.start((prop_constant * (color_sensor.get_reflected_light() - target_path)), movement_speed)


def main():
    target_path = 35
    prop_const = 4
    movement_speed = 75
    while True:
        pathfinder(target_path, prop_const, movement_speed)


if __name__ == '__main__':
    main()
