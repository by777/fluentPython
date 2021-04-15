# encoding =utf-8
import time
import multiprocessing


def mul(x):
    return x * x


if __name__ == "__main__":
    pool = multiprocessing.Pool(multiprocessing.cpu_count())  # start 4 worker processes
    result = pool.apply_async(mul, [100])
    # print(result)  # multiprocessing.pool.ApplyResult object
    # print(dir(result))
    print(result.get(timeout=10))  # 用get方法取出返回结果
    print(pool.map(mul, range(10)))
