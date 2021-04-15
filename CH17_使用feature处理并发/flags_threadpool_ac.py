# -*- coding: utf-8 -*-
# @TIME : 2021/4/15 10:37
# @AUTHOR : Xu Bai
# @FILE : flags_threadpool_ac.py
# @DESCRIPTION :
# -*- coding: utf-8 -*-
# @TIME : 2021/4/15 10:25
# @AUTHOR : Xu Bai
# @FILE : flags_threadpool.py
# @DESCRIPTION :
"""
concurrent.futures的主要特色是ThreadPoolExecutor和ProcessPoolExecutor类
这两类的接口能分别在不同的线程或进程中执行可调用的对象。
这两个类在内部维护着一个工作进程或线程池，以及要执行的任务队列
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
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduleed for {}: {}'
            print(msg.format(cc, future))
        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)
    # 获取结果数量，如果有线程抛出异常，会从这里抛出
    return len(list(res))


if __name__ == '__main__':
    main(download_many)
