import socket
from time import sleep
from services.delays import command_delays as delays

# IP and Port for Tello
tello_address = ("192.168.10.1", 8889)

# Create a UDP connection for Tello
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to local port
# sock.bind(("", 9000))

# control variables
distance = 0.2  # default distance for 'move' cmd
degrees = 30  # default degree for 'cw' or 'ccw' cmd


# Function to send Tello messages
def send_message(command):
    try:
        print("Sending: " + command)

        sock.sendto(command.encode(), tello_address)

    except Exception as e:
        print("Error sending: " + str(e))
        return close_sock()


def display_msg(msg):
    return print(msg)


def self_command():
    while True:
        send_message('command')
        sleep(0.5)


def tello_go_up():
    command = 'up %s' % distance
    return send_message(command)


def tello_go_down():
    command = 'down %s' % distance
    return send_message(command)


def tello_go_right():
    command = 'right %s' % distance
    return send_message(command)


def tello_go_left():
    command = 'left %s' % distance
    return send_message(command)


def tello_go_cw():
    command = 'cw %s' % degrees
    return send_message(command)


def tello_go_cww():
    command = 'ccw %s' % degrees
    return send_message(command)


def tello_flip(direction):
    command = 'flip %s' % direction
    return send_message(command)


# Get messages from Tello
def receive_response():
    try:
        response, ip_address = sock.recvfrom(1024)
        drone_state = response.decode(encoding='utf-8')
        msg = '{} state:\n {}'.format("Smart Eyes", drone_state.replace(';', ';\n'))
        return display_msg(msg)
    except Exception as e:
        print("Error receiving: " + str(e))
        return close_sock()


def stream_resp():
    try:
        while 1:
            response, ip = sock.recvfrom(1024)

            if response == 'ok':
                continue

            stream = response.decode(encoding='utf-8')
            msg = '{} state:\n {}'.format('Smart Eyes', stream.replace(';', ';\n'))
            display_msg(msg)

    except Exception as e:
        print("Error streaming: " + str(e))
        close_sock()


def close_sock():
    """
    close drone's communication socket
    :return:
    """
    return sock.close()


if __name__ == '__main__':
    drone = 'Smart Eyes'
    print(drone)
