import socket
import sys
import time

# Финальное задание
# задание: https://www.coursera.org/learn/diving-in-python/programming/aG3x3/kliient-dlia-otpravki-mietrik


class Socket:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip, self.port))

    def listen_message(self):
        while True:
            header = self.sock.recv(1024)
            if not len(header):
                sys.exit()
            try:
                header = header.decode('utf-8')
            except KeyError:
                self.sock.close()
                break
            else:
                if header:
                    return header

    def send_message(self, message):
        bytes = message.encode('utf-8')
        self.sock.send(bytes)
        return self.listen_message()

    def get_message(self, request):
        bytes = request.encode('utf-8')
        self.sock.send(bytes)
        return self.listen_message()


class ClientError(Exception):
    pass


class Client:
    def __init__(self, ip, port, timeout=None):
        self.timeout = timeout
        self.sock = Socket(ip, port)

    def _parse_message(self, message):
        data = {}
        if message.startswith('ok'):
            message = message.replace('ok\n', '')
            values = message.split('\n')

            if not values:
                return data
            for value in values:
                if not value:
                    continue

                name, value_name, timestamp = value.split(' ')
                if name in data:
                    data[name].append((int(timestamp), float(value_name)))
                else:
                    data[name] = [(int(timestamp), float(value_name))]

            return data
        else:
            raise ClientError

    def get(self, key):
        request_str = f'get {key}'
        try:
            message = self.sock.get_message(request_str)

            return self._parse_message(message)
        except Exception as e:
            raise e

    def put(self, key, value, timestamp=None):
        if not timestamp:
            timestamp = int(time.time())

        request_str = f'put {key} {value} {timestamp}'
        try:
            self.sock.send_message(request_str)
        except Exception:
            raise ClientError


# client = Client('127.0.0.1', 10001, timeout=15)
# client.put("palm.cpu", 0.5, timestamp=1150864247)
# client.put("ss.cpu", 0.5, timestamp=1150864247)
# client.put("ss.cpu", 0.6, timestamp=1150864247)
# print(client.get("*"))
# print(client.get("ss.cpu"))
