from src.controller.services.delays import command_delays as delays
from src.controller.services.drone_services import Drone
from time import sleep

'''
'takeoff', 'land'
'''

# Instantiate new Drone
tello = Drone('Tello')

command_list = ['command', 'battery?']
command_len = len(command_list)


for i in range(command_len):
    command = command_list[i]
    wait = delays[command]

    tello.send_msg(command)
    tello.recv_resp()

    sleep(wait)

tello.close_sock()
