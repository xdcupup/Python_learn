import threading

a =0
def func1():
    global a
    for i in range(100000):
        a+=1

def func2():
    global a
    for i in range(1000000):
        a+=1


if __name__ == '__main__':
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)

    t1.start()
    t1.join()

    t2.start()


    print(a)
