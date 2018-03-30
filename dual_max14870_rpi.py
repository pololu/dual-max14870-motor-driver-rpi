import pigpio

pi = pigpio.pi()
if not pi.connected:
  exit()

# Motor speeds for this library are specified as numbers between -MAX_SPEED and
# MAX_SPEED, inclusive.
# This has a value of 480 for historical reasons/to maintain compatibility with
# older versions of the library (which used WiringPi to set up the hardware PWM
# directly).
_max_speed = 480
MAX_SPEED = _max_speed

class Motor(object):
    MAX_SPEED = _max_speed

    def __init__(self, pwm_pin, dir_pin):
        self.pwm_pin = pwm_pin
        self.dir_pin = dir_pin

    def setSpeed(self, speed):
        if speed < 0:
            speed = -speed
            dir_value = 1
        else:
            dir_value = 0

        if speed > MAX_SPEED:
            speed = MAX_SPEED

        pi.write(self.dir_pin, dir_value)
        pi.hardware_PWM(self.pwm_pin, 20000, int(speed * 6250 / 3));
          # 20 kHz PWM, duty cycle in range 0-1000000 as expected by pigpio

class Motors(object):
    MAX_SPEED = _max_speed

    def __init__(self):
        self.motor1 = Motor(12, 24)
        self.motor2 = Motor(13, 25)

        pi.write(5, 0) # drive nEN low to enable drivers

    def setSpeeds(self, m1_speed, m2_speed):
        self.motor1.setSpeed(m1_speed)
        self.motor2.setSpeed(m2_speed)

motors = Motors()
