import threading


def coding():
    for i in range(10):
        print(f'coding{i}')

def sing():
    for i in range(10):
        print(f'sing{i}')

def sleeping():
    for i in range(10):
        print(f'sleeping{i}')

if __name__ == '__main__':


    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=sing)
    t3 = threading.Thread(target=sleeping)


    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()


