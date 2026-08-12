from commands import *


def send_command(command_queue, command_name, key="", value=""):
    message = {COMMAND_KEY: command_name}
    if key:
        message[key] = value
    command_queue.put(message)


def run_flight_sequence(command_queue, response_queue):
    send_command(command_queue, CMD_TAKE_OFF)
    send_command(command_queue, CMD_MOVE_UP)
    send_command(command_queue, CMD_ROTATE_LEFT, KEY_DEGREES, 90)
    send_command(command_queue, CMD_ROTATE_RIGHT, KEY_DEGREES, 45)
    send_command(command_queue, CMD_ROTATE_LEFT, KEY_DEGREES, 45)
    send_command(command_queue, CMD_LAND_IN_SAFE_PLACE)

    while True:
        response = response_queue.get()
        print("Acknowledged: {}".format(response))
        if response.get(SUCCESFULLY_PROCESSED_COMMAND_KEY) == CMD_LAND_IN_SAFE_PLACE:
            break
