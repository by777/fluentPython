# -*- coding: utf-8 -*-
# @TIME : 2021/4/15 10:25
# @AUTHOR : Xu Bai
# @FILE : flags_threadpool.py
# @DESCRIPTION :
"""
concurrent.futures的主要特色是ThreadPoolExecutor和ProcessPoolExecutor类
这两类的接口能分别在不同的线程或进程中执行可调用的对象。
这两个类在内部维护着一个工作进程或线程池，以及要执行的任务队列

！ 下载国旗的实例或其他密集IO型任务使用ProcessPoolExecutor类得不到任何好处
"""
from concurrent import futures

from flags import save_flag, get_flag, show, main

MAX_WORKERS = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))  # 从两者选取较小值，以免创建多余的线程
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))
    # 获取结果数量，如果有线程抛出异常，会从这里抛出
    return len(list(res))


if __name__ == '__main__':
    main(download_many)
