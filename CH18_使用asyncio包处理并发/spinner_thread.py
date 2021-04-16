# -*- coding: utf-8 -*-
# @TIME : 2021/4/15 21:02
# @AUTHOR : Xu Bai
# @FILE : spinner_thread.py
# @DESCRIPTION :
"""
对比一个简单的多线程程序和对应的asyncio版，说明多线程与异步任务之间的关系
"""
import itertools
import sys
import threading
import time


class Signal:
    # go属性用于外部控制线程
    go = True


def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        # 这实际是一个无限循环，会从中反复不断的生成元素
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        # 这是显示文本式动画的诀窍，可以使用退格符\x08把光标移回来
        time.sleep(.1)
        if not signal.go:
            break
    write(' ' * len(status) + '\x08' * len(status))


def slow_function():
    # 假设这是耗时的计算
    time.sleep(3)
    # 调用sleep会阻塞主线程，但一定要这么做，便于是刚GIL，创建从属线程
    return 42


def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking !', signal))
    print('spinner object: ', spinner)
    spinner.start()
    # 运行slowfunction会阻塞主线程，同时从属线程以动画形式显示旋转指针
    result = slow_function()
    # Python 没有提供终止线程的 API，这是有意为之的。若想关闭线
    # 程，必须给线程发送消息。这里，我使用的是 signal.go 属性：在主
    # 线程中把它设为 False 后，spinner 线程最终会注意到，然后干净地
    # 退出。
    signal.go = False
    spinner.join()  # 等待spinner线程结束
    return result


def main():
    result = supervisor()
    print('Answer: ', result)


if __name__ == '__main__':
    main()
