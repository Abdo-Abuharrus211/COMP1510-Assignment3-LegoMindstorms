from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, \
    not_equal_to
import math

# Create your objects here.
hub = MSHub()
movement_motors = MotorPair("B", "A")
distance_sensor = DistanceSensor("D")
color_sensor = ColorSensor("E")
propeller_motor = Motor("F")


def for_whom_the_bell_tolls(speed):
    """
    Commence shenanigans while remaining in bounds and RAM the enemy
    :param speed: integer representing movement speed
    :precondition: only accept integer values
    :postcondition: patrol arena and stay in bounds, RAM everything that moves!
    :return:
    """
    hub.speaker.beep()
    movement_motors.set_default_speed(speed)
    propeller_motor.start_at_power(speed)
    movement_motors.start()

    if color_sensor.get_color() == "black":
        movement_motors.move(-10, "cm", 20)
        movement_motors.move(320, "degrees", 100)
        movement_motors.move(20, "cm", 30)
        movement_motors.move(2, "rotations", 100)


def main():
    speed = 100
    while True:
        for_whom_the_bell_tolls(speed)


if __name__ == '__main__':
    main()
