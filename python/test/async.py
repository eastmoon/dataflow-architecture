# Async & Await execute method demo code.
# Python 3.5+ 開始可以使用 asyncio 標準庫和 await syntax 語法糖來寫 Coroutines：
# Python 3.7+ 開始可以使用 asyncio.run( )：
# Ref : https://docs.python.org/3/library/asyncio-task.html
# Ref : https://www.maxlist.xyz/2020/03/29/python-coroutine/
import asyncio
import types
import time
import random

now = lambda: time.time()

def type_check():
    def function():
        return 1

    def generator():
        yield 1

    async def async_function():
        return 1

    async def async_generator():
        yield 1

    print(type(function) is types.FunctionType)
    print(type(generator()) is types.GeneratorType)
    print(type(async_function()) is types.CoroutineType)
    print(type(async_generator()) is types.AsyncGeneratorType)

def async_demo():
    async def dosomething(num):
        print('第 {} 任務，第一步'.format(num))
        await asyncio.sleep(1 + 1 * random.random())
        print('第 {} 任務，第二步'.format(num))

    start = now()
    tasks = [dosomething(i) for i in range(5)]
    asyncio.run(asyncio.wait(tasks))
    print('TIME: ', now() - start)

def generator_async_demo():
    async def doOnes(num):
        print('第 {} 任務，第一步'.format(num))
        await asyncio.sleep(1)
        print('第 {} 任務，第二步'.format(num))

    async def do():
        await doOnes(1)
        time.sleep(5)
        await doOnes(2)
        print("DONE")

    asyncio.run(do())

async_demo()
generator_async_demo()
