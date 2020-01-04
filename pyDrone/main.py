from services.delays import command_delays as delays
from services.drone_services import Drone
from time import sleep
import sys

command_args = sys.argv
argument_list = command_args[1:]
command_len = len(argument_list)

# Instantiate new Drone
tello = Drone('Tello')

for i in range(command_len):
    command = argument_list[i]
    wait = delays[command]

    tello.send_msg(command)
    tello.stream_resp()

    sleep(wait)


tello.close_sock()


if __name__ == '__main__':
    print('We got called')
    sys.stdout.flush()
