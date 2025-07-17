from queue import Queue
from threading import Thread
import time

# 创建一个生产者类
class Producer(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(1, 6):
            print(f'{self.name}将产品{i}放入队列')
            self.queue.put(i)
            time.sleep(1)
        print('生产者完成了所有数据的存放')

# 创建一个消费者类
class Consumer(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self, name=name)
        self.queue = queue
    def run(self):
        for i in range(5):
            value=self.queue.get()
            print(f'消费者线程：{self.name}取出了{value}')
            time.sleep(1)
        print('------------------消费者线程取出了所有的数据----------------')
if __name__ == '__main__':
    queue = Queue()
    p=Producer('producer', queue)
    c=Consumer('consumer', queue)
    p.start()
    c.start()
    p.join()
    c.join()