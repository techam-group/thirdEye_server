# from servicess.delays import command_delays as delays
# from servicess.drone_services import Drone
import sys

'''
'takeoff', 'land', 'time?', 'speed?',
'''

import src.services.delays as delays

print(delays)

# command_list = ['command', 'battery?']
# command_len = len(command_list)
#
# print(command_list)
#
# # Instantiate new Drone
# tello = Drone('Tello', command_len)
#
#
# for i in range(command_len):
#     command = command_list[i]
#     wait = delays[command]
#
#     tello.send_msg(command)
#     tello.stream_resp()
#
#     sleep(wait)
#
#
# tello.close_sock()


if __name__ == '__main__':
    print('We got called')
    sys.stdout.flush()
