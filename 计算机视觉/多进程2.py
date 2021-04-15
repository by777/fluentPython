from multiprocessing import Pool


def f(object):
    return object.x * object.y


class A:
    def __init__(self, a, b):
        self.x = a
        self.y = b


if __name__ == '__main__':
    pool = Pool(processes=4)  # start 4 worker processes
    params = [A(i, i) for i in range(10)]

    print(params)
    print(pool.map(f, params))  # prints "[0, 1, 4,..., 81]"
    print(pool)
