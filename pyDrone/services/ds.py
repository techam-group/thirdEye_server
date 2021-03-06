# _3rd_eyes servicess
import socket


class Drone:
    def __init__(self, name="Smart Eyes", count=1):
        """
        This is an instance of our Third_Eye drone. We are using Tello Drone for testing, but hopefully you should run
        this code with any drone out there.
        :type name: string
        """
        self.name = name
        self.count = count
        self.local_ip = ''
        self.local_port = 8890
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.drone_ip = '192.168.10.1'
        self.drone_port = 8889
        self.drone_addr = (self.drone_ip, self.drone_port)

        self.create_local_socket()

    def create_local_socket(self):
        return self.sock.bind((self.local_ip, self.local_port))

    def send_msg(self, msg):
        try:
            print('Sending ' + msg)
            return self.sock.sendto(msg.encode(), self.drone_addr)
        except Exception as e:
            print('Error sending message: ' + str(e))
            return self.close_sock()

    @staticmethod
    def display_msg(msg):
        return print(msg)

    def recv_resp(self):
        try:
            resp, ip_addr = self.sock.recvfrom(1024)

            drone_state = resp.decode(encoding='utf-8')
            msg = '{} state:\n {}'.format(self.name, drone_state.replace(';', ';\n'))
            return self.display_msg(msg)

        except Exception as e:
            print("Error receiving: " + str(e))
            self.close_sock()

    def stream_resp(self):
        try:
            count = 0
            while count <= self.count:
                resp, ip = self.sock.recvfrom(1024)

                if resp == 'ok':
                    continue

                stream = resp.decode(encoding='utf-8')
                msg = '{} state:\n {}'.format(self.name, stream.replace(';', ';\n'))
                self.display_msg(msg)

                count += 1

        except Exception as e:
            print("Error streaming: " + str(e))
            self.close_sock()

    def close_sock(self):
        """
        close drone's communication socket
        :return:
        """
        return self.sock.close()


if __name__ == '__main__':
    drone = Drone()
    print(drone.name)
