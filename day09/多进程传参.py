import multiprocessing
import random


def func(windows_num,num):
    print(f'窗口{windows_num}')
    for i in range(num):
        print(f'车票{i}')


if __name__ == '__main__':
    data_list = []
    for i in range(10):
        p = multiprocessing.Process(target=func,args=(i+1,random.randint(20,50)))
        data_list.append(p)

    for i in data_list:
        i.start()

        print('begin')