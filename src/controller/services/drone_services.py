# _3rd_eyes services
import socket
from time import sleep

# Setup the ports and addresses for local communication
local_ip = ''
local_port = 8890
tello = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello.bind((local_ip, local_port))

# Setup thirdEye ports and addresses for flight communication
_3rd_eye_ip = '192.168.10.1'
_3rd_eye_port = 8889
_3rd_eye_addr = (_3rd_eye_ip, _3rd_eye_port)


# Send messages function
def send_msg(message):
    try:
        tello.sendto(message.encode(), _3rd_eye_addr)
        print('Sent ' + message)
    except Exception as e:
        print('Error sending: ' + str(e))


# Receive responses from _3rd_eye
def display_msg(message):
    try:
        print(message)
    except Exception as e:
        print('Error receiving message: ' + str(e))


def recv_resp():
    try:
        resp, ip_addr = tello.recvfrom(1024)

        tello_state = resp.decode(encoding='utf-8')
        message = 'Tello State:\n' + tello_state.replace(';', ';\n')
        display_msg(message)

    except Exception as e:
        print("Error receiving: " + str(e))
        close_sock()


def close_sock():
    tello.close()
