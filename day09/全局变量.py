import multiprocessing

data = [1,2,3,4]

def func1():
    data.append(5)
    print(id(data))

def func2():
    print(data)
    print(id(data))


if __name__ == '__main__':

    p1 = multiprocessing.Process(target=func1)
    p2 = multiprocessing.Process(target=func2)

    p1.start()
    p2.start()
