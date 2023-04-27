import threading


def dance():
    print('子线程1')
    for i in range(10):
        print(f'dance{i}')

def sing():
    print('子线程2')
    for i in range(10):
        print(f'sing{i}')


if __name__ == '__main__':
    t1 = threading.Thread(target=dance)
    t2 = threading.Thread(target=sing)

    t1.start()
    t2.start()

    print('主线程')