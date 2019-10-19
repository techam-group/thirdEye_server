from services import delays
from services import drone_services as ds
from time import sleep

'''
'takeoff', 'land'
'''

command_list = ['command', 'battery?']
command_len = len(command_list)

for i in range(command_len):
    command = command_list[i]
    waait = delays.command_delays[command]

    ds.send_msg(command)
    ds.recv_resp()

    sleep(waait)

ds.close_sock()
