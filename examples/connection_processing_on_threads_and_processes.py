# обработка нескольких соединений одновременно, процессы и потоки
import os
import socket
import threading
import multiprocessing


def process_request(conn, addr):
    print("connected client:", addr)
    with conn:
        # поток для обработки соединения
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode("utf8"))


# Как обычно, мы создаем socket, вызываем методы bind и listen.
# Затем мы должны при помощи модуля multiprocessing создать несколько объектов worker,
# которые будут обрабатывать новые соединения.

# Давайте рассмотрим код наших worker-ов.
# Итак, каждый worker, который будет запущен в отдельном процессе, делает системный вызов accept.
# Все входящие соединения будут равномерно распределены между worker-ами при помощи операционной системы.
# И после того как соединение попало в наш процесс, необходимо создать поток и передать
# ему метод process_request, который обрабатывает данное соединение:
def worker(sock):
    while True:
        # accept распределится "равномерно" между процессами
        conn, addr = sock.accept()
        print("pid", os.getpid())
        th = threading.Thread(target=process_request, args=(conn, addr))
        th.start()


with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()

    workers_count = 3
    # создание нескольких процессов
    workers_list = [multiprocessing.Process(target=worker, args=(sock,))
                    for _ in range(workers_count)]

    for w in workers_list:
        w.start()

    for w in workers_list:
        w.join()
