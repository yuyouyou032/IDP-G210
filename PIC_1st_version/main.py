from test_motor import motor_left, motor_right, turn_off
from test_button_LED import sensor12
from utime import sleep

pin_MR = 12  # middle-right (front)
pin_ML = 13  # middle-left (front)
pin_FR = 7   # far-right (rear)
pin_FL = 8   # far-left (rear)

class LinePID:
    def __init__(self, Kp=40.0, Ki=0.0, Kd=12.0, base_speed=70, dt=0.05):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.base_speed = base_speed
        self.dt = dt
        self.integral = 0
        self.prev_error = 0

    def update(self, ML, MR):
        if ML == 1 and MR == 1:
            error = 0      # centered
        elif ML == 1 and MR == 0:
            error = +1     # line shifted to right, turn left
        elif ML == 0 and MR == 1:
            error = -1     # line shifted to left, turn right
        else:
            error = self.prev_error  # lost line, keep last error

        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error = error

        left_speed = max(0, min(100, self.base_speed - output))
        right_speed = max(0, min(100, self.base_speed + output))

        motor_left.Forward(int(left_speed))
        motor_right.Forward(int(right_speed))

        return error, int(left_speed), int(right_speed)

pid = LinePID(Kp=40, Ki=0, Kd=12, base_speed=70, dt=0.05)

def read_middle_sensors():
    ML, MR = sensor12(pin_ML, pin_MR)
    return ML, MR

def read_all_sensors():
    ML, MR = sensor12(pin_ML, pin_MR)
    FL, FR = sensor12(pin_FL, pin_FR)
    return MR, ML, FR, FL

print("Starting line-following car...")

while True:
        MR, ML, FR, FL = read_all_sensors()
        print("Sensors [FL, ML, MR, FR]:", [FL, ML, MR, FR])

        # --- Junction detection (rear sensors) ---
        if FL == 1:
            print("LEFT junction detected -> CCW turn")
            motor_left.off()
            motor_right.Forward(40)
            sleep(0.25)
            continue

        if FR == 0:
            print("RIGHT junction detected -> CW turn")
            motor_left.Forward(40)
            motor_right.off()
            sleep(0.25)
            continue

        error, left_speed, right_speed = pid.update(ML, MR)
        print("PID -> Error:", error, "Left:", left_speed, "Right:", right_speed)

        sleep(pid.dt)
