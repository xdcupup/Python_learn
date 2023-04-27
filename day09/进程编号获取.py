import multiprocessing
import os


def dance():
    pid = os.getpid()
    print(f'子进程1编号:{pid}')
    ppid = os.getppid()
    print(f'子进程1-父进程编号{ppid}')
    print('dance_begin')
    # for i in range(10):
    #     print(f'dance{i}')

def sing():
    pid = os.getpid()
    print(f'子进程2编号:{pid}')
    ppid = os.getppid()
    print(f'子进程2-父进程编号{ppid}')
    print('sing_begin')
    # for i in range(10):
    #     print(f'sing{i}')


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=dance)
    p2 = multiprocessing.Process(target=sing)

    p1.start()
    p2.start()

    print('主进程')
    print('观看表演')
    print(__name__)
