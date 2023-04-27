# 请使用多任务形式完成：一边编程、一边听音乐、一边跟同事聊天。要求如下：
# 		a.使用多进程完成；
# 		b.使用多线程完成；
# 		c.分别观察与对比多进程、多线程的执行效果。
import threading


# 多进程
def coding():
    print('进程coding开始')
    for i in range(10):
        print(f'coding{i}')

def music():
    print('进程music开始')
    for i in range(10):
        print(f'music{i}')

def chat():
    print('进程chat开始')
    for i in range(10):
        print(f'chat{i}')


if __name__ == '__main__':
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=music)
    t3 = threading.Thread(target=chat)




    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()