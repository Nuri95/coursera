# asyncio, Hello World

import asyncio


@asyncio.coroutine  # делает нашу функцию корутиной
def hello_world():
    while True:
        print("Hello World!")
        # мы в бесконечном цикле выполняем вывод строчки "Hello World" в консоль

        # делаем вызов yield from для того, чтобы наша корутина приостановила свою работу,
        # тем самым давая возможность поисполняться другим корутинам
        yield from asyncio.sleep(1.0)


loop = asyncio.get_event_loop()  # мы получаем цикл обработки событий
# Это объект, который исполняет корутины
# (обычные функции с помощью него исполнять нельзя, нужно использовать именно корутины):


loop.run_until_complete(hello_world())
loop.close()