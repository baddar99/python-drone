from commands import *


class Drone:
    def __init__(self, name):
        self.name = name
        self.min_altitude = 0
        self.max_altitude = 30

    def print_with_name_prefix(self, message):
        print("{}: {}".format(self.name, message))

    def take_off(self):
        self.print_with_name_prefix("Taking off")

    def land(self):
        self.print_with_name_prefix("Landing")

    def land_in_safe_place(self):
        self.print_with_name_prefix("Landing in a safe place")

    def move_up(self):
        self.print_with_name_prefix("Moving up")

    def move_down(self):
        self.print_with_name_prefix("Moving down")

    def move_forward(self):
        self.print_with_name_prefix("Moving forward")

    def move_back(self):
        self.print_with_name_prefix("Moving back")

    def move_left(self):
        self.print_with_name_prefix("Moving left")

    def move_right(self):
        self.print_with_name_prefix("Moving right")

    def rotate_right(self, degrees):
        self.print_with_name_prefix(
            "Rotating right {} degrees".format(degrees))

    def rotate_left(self, degrees):
        self.print_with_name_prefix(
            "Rotating left {} degrees".format(degrees))

    def set_max_altitude(self, feet):
        self.max_altitude = feet
        self.print_with_name_prefix(
            "Setting maximum altitude to {} feet".format(feet))

    def set_min_altitude(self, feet):
        self.min_altitude = feet
        self.print_with_name_prefix(
            "Setting minimum altitude to {} feet".format(feet))


class DroneCommandProcessor:
    # lives in the drone's process, pulls commands off the queue and
    # pushes acks back on the other one
    def __init__(self, drone, command_queue, response_queue):
        self.drone = drone
        self.command_queue = command_queue
        self.response_queue = response_queue

    def run(self):
        while True:
            message = self.command_queue.get()
            if message is None:
                break
            self.process_command(message)

    def process_command(self, message):
        command = message.get(COMMAND_KEY)
        is_command_processed = True

        if command == CMD_TAKE_OFF:
            self.drone.take_off()
        elif command == CMD_LAND:
            self.drone.land()
        elif command == CMD_LAND_IN_SAFE_PLACE:
            self.drone.land_in_safe_place()
        elif command == CMD_MOVE_UP:
            self.drone.move_up()
        elif command == CMD_MOVE_DOWN:
            self.drone.move_down()
        elif command == CMD_MOVE_FORWARD:
            self.drone.move_forward()
        elif command == CMD_MOVE_BACK:
            self.drone.move_back()
        elif command == CMD_MOVE_LEFT:
            self.drone.move_left()
        elif command == CMD_MOVE_RIGHT:
            self.drone.move_right()
        elif command == CMD_ROTATE_RIGHT:
            self.drone.rotate_right(message[KEY_DEGREES])
        elif command == CMD_ROTATE_LEFT:
            self.drone.rotate_left(message[KEY_DEGREES])
        elif command == CMD_SET_MAX_ALTITUDE:
            self.drone.set_max_altitude(message[KEY_FEET])
        elif command == CMD_SET_MIN_ALTITUDE:
            self.drone.set_min_altitude(message[KEY_FEET])
        else:
            is_command_processed = False
            print("Unknown command: {}".format(command))

        if is_command_processed:
            self.response_queue.put(
                {SUCCESFULLY_PROCESSED_COMMAND_KEY: command})
