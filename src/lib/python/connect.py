import socket
from time import sleep

# IP and Port for Tello
tello_address = ("192.168.10.1", 8889)

# Create a UDP connection for Tello
sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to local port
sock_udp.bind(("", 9000))

# Function to send Tello messages
def send_message(message):
  try:
    sock_udp.sendto(message.encode(), tello_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))


# Get messages from Tello
def recieve_response():
  try:
    response, ip_address = sock_udp.recvfrom(128)
    print(
      "Received message: "
      + response.decode(encoding="utf-8")
      + " from Tello wit IP: "
      + str(ip_address)
    )
  except Exception as e:
    print("Error receiving: " + str(e))


# Send Tello commands
send_message("command")

# Recieve responses from Tello
recieve_response()

# Delay seconds before sending next command
sleep(3)

# Ask for battery status
send_message("battery?")

recieve_response()

# Tello takeoff
sleep(5)
send_message('takeoff')
recieve_response()

# Tello land
sleep(5)
send_message('land')
recieve_response()

# Close UDP socket
sock_udp.close()
