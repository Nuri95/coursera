# asyncio, tcp сервер
# напишем свой TCP-сервер, который обрабатывает несколько входящих соединений одновременно

import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(1024)  # мы можем читать данные из нашего сокета
    message = data.decode()
    addr = writer.get_extra_info("peername")
    print("received %r from %r" % (message, addr))
    writer.close()


loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, "127.0.0.1", 10001, loop=loop)
server = loop.run_until_complete(coro)
try:
    loop.run_forever()
#     мы будем обрабатывать все входящие соединения, и после того, как мы заакцептили соединение,
#     для каждого соединения будет создана отдельная корутина, и в этой корутине будет выполнена наша функция
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()