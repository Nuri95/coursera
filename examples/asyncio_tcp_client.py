# asyncio, tcp клиент
# асинхронный клиент

# Допустим, клиент будет передавать строчку.
# В корутину tcp_echo_client передаём эту строчку (message) и наш event loop.
# Далее, для того, чтобы создать соединение, мы должны вызвать метод asyncio.open_connection.
# В этом вызове мы должны отправить адресную пару и вызов await вернет нам reader и writer.


import asyncio

async def tcp_echo_client(message):
    try:
        reader, writer = await asyncio.open_connection(
            '127.0.0.1', 10001)

        print(f'Send: {message!r}')
        writer.write(message.encode())
        await writer.drain()

        while True:
            data = await reader.read(100)
            print(f'Received: {data.decode()!r}')
            text = input()
            writer.write(text.encode())
            await writer.drain()


        print('Close the connection')
        writer.close()
    except Exception as e:
        print(1111111111)

asyncio.run(tcp_echo_client('Hello World!'))