from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, \
    not_equal_to
import math

# Create your objects here.
hub = MSHub()
movement_motors = MotorPair("A", "B")
distance_sensor = DistanceSensor("D")
color_sensor = ColorSensor("E")
lifting_arm = Motor("C")


def radar_style_finder(speed, time_seconds):
    """
    Rotate robot and catch ball with crab arm then clasp it with drop arm
    :param speed: integer value representing rotation speed
    :param time_seconds: integer value representing rotation duration
    :precondition: only accept integer values
    :postcondition: rotate ball clockwise and clasp ball after specified duration
    """
    hub.speaker.beep()
    lifting_arm.run_to_position(100, 'shortest path', 80)
    movement_motors.start(100, speed)  # start swipe
    wait_for_seconds(9)
    lifting_arm.run_to_position(160, 'shortest path', 10)
    movement_motors.stop()


def main():
    speed = 15
    time_seconds = 9
    radar_style_finder(speed, time_seconds)


if __name__ == '__main__':
    main()
