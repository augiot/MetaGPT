"""
让我们通过一个简单的例子来展示Python中协程和同步代码的对比。我们将编写一个程序，该程序的任务是打印数字序列，但每个数字打印之间会有一个短暂的延迟。
"""

"""
同步代码示例:
在同步代码中，我们使用普通的函数和time.sleep()来模拟延迟。
"""

import time

def print_numbers_sync():
    for i in range(1, 6):
        print(i)
        time.sleep(1)  # 模拟耗时操作

print("同步代码开始执行")
# print_numbers_sync()
print("同步代码执行完毕")


"""
协程代码示例
在协程代码中，我们使用async和await来定义和调用异步函数。这里使用asyncio.sleep()来模拟异步延迟。
"""

import asyncio

async def print_numbers_coroutine():
    for i in range(1, 6):
        print(i)
        await asyncio.sleep(1)  # 模拟异步耗时操作

async def main():
    print("协程代码开始执行")
    await print_numbers_coroutine()
    print("协程代码执行完毕")

# 运行协程
# asyncio.run(main())
"""
对比分析

执行流程：
同步代码：print_numbers_sync()函数会按顺序打印数字，每打印一个数字后暂停1秒，直到所有数字打印完毕。
协程代码：print_numbers_coroutine()函数在打印每个数字后会使用await asyncio.sleep(1)，这允许其他协程在等待时运行。
性能：
在I/O密集型或需要并发执行多个任务的场景中，协程通常比同步代码更高效，因为它们可以在等待时让出控制权，允许其他任务执行。
代码复杂性：
同步代码更简单直观，易于理解。
协程代码需要使用async和await，对于初学者来说可能稍微复杂一些。
适用场景：
同步代码适用于简单的顺序执行任务，或者计算密集型任务。
协程代码适用于需要高并发处理的任务，如网络请求、文件I/O等。
请注意，为了运行协程代码，你需要Python 3.5或更高版本，因为async和await是在这个版本中引入的。而同步代码可以在任何Python版本中运行。
"""


import asyncio

async def print_numbers_concurrently(n, prefix=""):
    for i in range(n):
        print(f"{prefix} {i + 1}")
        await asyncio.sleep(1)  # 模拟异步耗时操作
    return f"{prefix} 完成"

async def print_numbers_concurrently_2(n, prefix=""):
    for i in range(n):
        print(f"{prefix} {i + 1}")
        await asyncio.sleep(1)
    return f"{prefix} 完成"


async def main_2():
    print("协程并发执行开始")

    # 创建两个协程任务
    task1 = asyncio.create_task(print_numbers_concurrently(5, "Task 1:"))
    task2 = asyncio.create_task(print_numbers_concurrently(5, "Task 2:"))

    # 等待两个协程任务完成
    await task1
    await task2

    print("协程并发执行完毕")

# 运行主函数
# asyncio.run(main_2()



async def main_3():
    print("协程并发执行开始")
    for i in range(2):
        await print_numbers_concurrently(5, f"Task {i + 1}:")

    print("协程并发执行完毕")

# asyncio.run(main_3())


async def main_4():
    print("开始执行异步操作")

    # 创建一个任务列表，每个任务都是一个异步操作
    tasks = [print_numbers_concurrently(5,"Tasks:") for i in range(5)]
    print(tasks)
    # 使用 asyncio.gather 并发执行所有任务
    results = await asyncio.gather(*tasks)

    # 打印结果
    for result in results:
        print(result)

    print("异步操作完成")

# asyncio.run(main_4())

async def main_5():
    for i in range(2):
        await print_numbers_concurrently_2(5, f"Task {i + 1}:")

asyncio.run(main_5())

"""
https://www.jb51.net/article/235010.htm
"""