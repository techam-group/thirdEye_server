from services.delays import command_delays as delays
from services.drone_services import Drone
from time import sleep
import sys

'''
'takeoff', 'land', 'time?', 'speed?',
'''

command_list = ['command', 'battery?', 'takeoff', 'land']
command_len = len(command_list)

print(command_list)

# Instantiate new Drone
tello = Drone('Tello', command_len)


for i in range(command_len):
    command = command_list[i]
    wait = delays[command]

    tello.send_msg(command)
    tello.stream_resp()

    sleep(wait)


tello.close_sock()


# if __name__ == '__main__':
#     print('We got called')
#     sys.stdout.flush()
