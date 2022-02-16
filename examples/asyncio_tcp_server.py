# asyncio, tcp сервер

import asyncio


async def handle_echo(reader, writer):
    while True:
        try:
            data = await reader.read(100)
            if not data:
                print('Client died...')
                break

            message = data.decode()
            addr = writer.get_extra_info('peername')

            print(f"Received {message!r} from {addr!r}")

            print(f"Send: {message!r}")
            writer.write(data)
            await writer.drain()
        except KeyboardInterrupt:
            writer.close()
            break
        except Exception as e:
            print(e, '___________________')

    print("Close the connection")
    writer.close()


async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 10001
    )

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())