import socket
from threading import Thread


class Server:
    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, port))
        self.sock.listen(5)
        self.daemon = True
        super().__init__()
        self.data = {}

    def listen_connection(self):
        print('сервер слушает')
        while True:
            client_socket, client_address = self.sock.accept()
            handle = HandleConnectionThread(client_socket, self.data)
            handle.start()


class HandleConnectionThread(Thread):
    def __init__(self, sock, data):
        self.sock = sock
        super().__init__()
        self.daemon = True
        self.data = data

    def run(self):
        try:
            self.listen_message()
        except Exception as e:
            print(str(e))

    def _serialize(self, message):
        _, key = message.split(' ')

        print('get запрос получил')

        message = 'ok\n'
        if key == '*':
            for key, data in self.data.items():
                for i in data:
                    message += f'{key} {i}\n'
        elif key in self.data:
            for i in self.data[key]:
                message += f'{key} {i}\n'

        message += '\n'
        return message.encode('utf-8')

    def listen_message(self):
        while True:
            header = self.sock.recv(100)
            if not len(header):
                continue

            message = header.decode('utf-8')

            if message.startswith('get'):

                self.sock.send(self._serialize(message))
            else:
                method, key, value, time = message.split()

                if method == 'put' and key not in self.data:
                    self.data[key] = [f'{value} {time}']
                elif method == 'put':
                    self.data[key].append(f'{value} {time}')

                print('сервер ответил ok')
                self.sock.send(b'ok')


def run_server(ip, port):
    server = Server(ip, port)
    try:
        server.listen_connection()
    except Exception as e:
        raise e


run_server('127.0.0.1', 10001)
print('сервер перестал слушать')
