import multiprocessing


def dance():
    print('dance_begin')
    for i in range(10):
        print(f'dance{i}')

def sing():
    print('sing_begin')
    for i in range(10):
        print(f'sing{i}')


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=sing)
    p2 = multiprocessing.Process(target=dance)

    p1.start()
    p2.start()

    print('主进程')
    print('观看表演')
    print(__name__)
