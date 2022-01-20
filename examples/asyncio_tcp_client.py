# asyncio, tcp клиент
# асинхронный клиент

# Допустим, клиент будет передавать строчку.
# В корутину tcp_echo_client передаём эту строчку (message) и наш event loop.
# Далее, для того, чтобы создать соединение, мы должны вызвать метод asyncio.open_connection.
# В этом вызове мы должны отправить адресную пару и вызов await вернет нам reader и writer.


import asyncio


async def tcp_echo_client(message, loop):
    # два объекта, при помощи которых можно взаимодействовать с нашим удаленным сервером.
    # при помощи объекта reader можно читать данные с сервера,
    # при помощи объекта writer можно записывать данные на сервер
    reader, writer = await asyncio.open_connection("127.0.0.1", 10001, loop=loop)

    print("send: %r" % message)
    writer.write(message.encode())
    writer.close()

loop = asyncio.get_event_loop()
message = "hello World!"
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()
