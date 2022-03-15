import asyncio
import sys


# Задание: https://www.coursera.org/learn/diving-in-python/programming/Xcdpa/siervier-dlia-priiema-mietrik
# Сервер для приема метрик

# 1 способ: с классом
class ClientServerProtocol(asyncio.Protocol):
    data = {}

    def _get_error_message(self):
        return 'error\nwrong command\n'

    def _serialize(self, data):
        return data.encode('utf-8')

    def _get_report(self, message):
        try:
            _, key = message.split(' ')
        except Exception:
            return self._get_error_message()

        message = 'ok\n'
        key = key.replace('\r\n', '')
        if key == '*':
            for key, data in self.data.items():
                for time, value in data.items():
                    message += f'{key} {value} {time}\n'
        elif key in self.data:
            for time, value in self.data[key].items():
                message += f'{key} {value} {time}\n'

        message += '\n'
        return message

    def _process_data(self, message):
        try:
            if message.startswith('get'):
                data = self._get_report(message)
            elif message.startswith('put'):
                method, key, value, time = message.split()

                if method == 'put' and key not in self.data:
                    self.data[key] = {time: value}
                elif method == 'put':
                    if time in self.data[key]:
                        self.data[key][time] = value
                    else:
                        self.data[key].update({time: value})

                    # await asyncio.sleep(10)

                data = 'ok'
            else:
                data = self._get_error_message()

            return self._serialize(data)
        except Exception as e:
            print(e)
            raise e

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        data = self._process_data(data.decode())
        self.transport.write(data)


async def main():
    loop = asyncio.get_running_loop()
    server = await loop.create_server(
        ClientServerProtocol,
        '127.0.0.1',
        10001,
    )
    async with server:
        await server.serve_forever()

try:
    asyncio.run(main())
except Exception as e:
    print(e)
    sys.exit(1)


# 2 способ решения: без класса

history = {}


def get_error_message():
    return b'error\nwrong command\n'


def get_report(message):
    print(message)
    try:
        _, key = message.split(' ')
    except Exception:
        return get_error_message()

    message = 'ok\n'
    if key == '*':
        for key, data in history.items():
            print('data=', data)
            for time, value in data.items():
                message += f'{key} {value} {time}\n'
    elif key in history:
        for time, value in history[key].items():
            message += f'{key} {value} {time}\n'

    message += '\n'
    return message.encode('utf-8')


async def handle_connection(reader, writer):
    peername = writer.get_extra_info('peername')
    print('Принято соединение от ', peername)
    while True:
        try:
            message = (await reader.read(1024)).decode()
            if not message:
                print('client died')
                break

            if message.startswith('get'):
                writer.write(get_report(message))
            elif message.startswith('put'):
                method, key, value, time = message.split()

                if method == 'put' and key not in history:
                    history[key] = {time: value}
                elif method == 'put':
                    if time in history[key]:
                        history[key][time] = value
                    else:
                        history[key].update({time: value})

                # await asyncio.sleep(5)
                writer.write(b'Ok')
            else:
                writer.write(get_error_message())

            await writer.drain()
        except KeyboardInterrupt:
            writer.close()
            break
        except Exception as e:
            raise e

    writer.close()


# async def main():
#     server = await asyncio.start_server(
#         handle_connection,
#         '127.0.0.1',
#         10001
#     )
#
#     async with server:
#         await server.serve_forever()
#
#
# asyncio.run(main())
