# -*- coding: utf-8 -*-
# @TIME : 2021/4/15 21:02
# @AUTHOR : Xu Bai
# @FILE :
# @DESCRIPTION :

import asyncio
import itertools
import sys


# 打算交给asyncio处理的协程要用@asyncio.coroutine 装饰。
# 这不是强制要求，但这样能在一众普通的函数中把协程凸显出来，也有助于调试：
# 如果还没从中产出值，协程就被垃圾回收了（意味着有操作未完成，因
# 此有可能是个缺陷），那就可以发出警告。这个装饰器不会预激协程。
@asyncio.coroutine
def spin(msg):
    # 这里不需要用来关闭线程的signal参数
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            # 这样的休眠不会阻塞事件循环。
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
        write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def slow_function():
    # 现在，slow_function 函数是协程，在用休眠假装进行 I/O 操作
    # 时，使用 yield from 继续执行事件循环。
    # 假装等待I/O一段时间
    yield from asyncio.sleep(3)
    return 42


@asyncio.coroutine
def supervisor():
    # asyncio.async(...) 函数排定 spin 协程的运行时间，使用一个
    # Task 对象包装 spin 协程，并立即返回。
    #
    # 这里有兼容性问题
    spinner = asyncio.async(spin('thinking!'))
    print('spinner object: ', spinner)
    result = yield from slow_function()
    spinner.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer: ', result)


if __name__ == '__main__':
    main()
    print('除非想阻塞主线程，'
          '从而冻结事件循环或整个应用，'
          '否则不要在 asyncio 协程中使用 time.sleep(...)。'
          '如果协程需要在一段时间内什么也不做，'
          '应该使用 yield from asyncio.sleep(DELAY)。')
