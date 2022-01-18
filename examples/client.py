# создание сокета, таймауты и обработка ошибок
# клиент
import socket
import time

with socket.create_connection(("127.0.0.1", 10001), 5) as sock:
    # set socket read timeout
    sock.settimeout(2)
    try:
        sock.sendall("ping".encode("utf8"))
        sock.sendall("ping2".encode("utf8"))
        time.sleep(3)
        sock.sendall("ping3/3".encode("utf8"))
        time.sleep(5)
        sock.sendall("ping3".encode("utf8"))
        time.sleep(8)
        sock.sendall("ping4".encode("utf8"))
    except socket.timeout:
        print("send data timeout")
    except socket.error as ex:
        print("send data error:", ex)
    except Exception as e:
        print(str(e))