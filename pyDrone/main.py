from services.delays import command_delays as delays
import services.drone_services as ds
from time import sleep
import sys

command_args = sys.argv
command = command_args[1:][0]

# control variables
distance = 0.1  # default distance for 'move' cmd
degrees = 30  # default degree for 'cw' or 'ccw' cmd

if command == 'command':
    wait = delays[command]
    sleep(wait)
    ds.send_message(command)

if command == 'takeoff':
    wait = delays[command]
    sleep(wait)
    ds.send_message(command)

if command == 'land':
    wait = delays[command]
    sleep(wait)
    ds.send_message(command)

if command == 'up':
    wait = delays[command]
    sleep(wait)
    ds.tello_go_up()

if command == 'down':
    wait = delays[command]
    sleep(wait)
    ds.tello_go_down()

if command == 'right':
    wait = delays[command]
    sleep(wait)
    ds.tello_go_right()

if command == 'left':
    wait = delays[command]
    sleep(wait)
    ds.tello_go_left()

if command == 'cw':
    wait = delays[command]
    sleep(wait)
    ds.tello_go_cw()

if command == 'ccw':
    wait = delays[command]
    sleep(wait)
    ds.tello_go_cww()

if command == 'l' or command == 'r' or command == 'f' or command == 'b':
    if command == 'l':
        wait = delays['left']
        sleep(wait)
        ds.tello_flip(command)
    elif command == 'r':
        wait = delays['right']
        sleep(wait)
        ds.tello_flip(command)
    elif command == 'f':
        wait = delays['forward']
        sleep(wait)
        ds.tello_flip(command)
    elif command == 'b':
        wait = delays['back']
        sleep(wait)
        ds.tello_flip(command)


ds.stream_resp()
ds.close_sock()


if __name__ == '__main__':
    print('We got called')
    sys.stdout.flush()
