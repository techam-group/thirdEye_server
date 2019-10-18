import socket
from time import sleep

INTERVAL = 0.2

def send_msg(sock, message, tello_addrs):
  try:
    sock.sendto(message.encode(), tello_addrs)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))


def recv_msg(message):
  try:
    print(message)
  except Exception as e:
    print('Error recieving message: ' + str(e))


if __name__ == "__main__":
  local_ip = ''
  local_port = 8890
  local_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  local_socket.bind((local_ip, local_port))

  tello_ip = '192.168.10.1'
  tello_port = 8889
  tello_adderss = (tello_ip, tello_port)

  send_msg(local_socket, 'command', tello_adderss)

  # socket.sendto('command'.encode(), tello_adderss)

  index = 0

  while True:
    index += 1
    response, ip = local_socket.recvfrom(1024)
    if response == 'ok':
      continue
    out = response.decode(encoding='utf-8')
    # formatted_output = out.replace(';', ';\n')
    # out = 'Tello State: ' + formatted_output
    out = 'Tello State: ' + out
    recv_msg(out)
    sleep(INTERVAL)
