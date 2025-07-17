from copy import deepcopy


class CPU():
    pass
class Disk():
    pass
class Computer():
    # 计算机由CPU和硬盘
    def __init__(self,cpu, disk):
        self.cpu=cpu
        self.disk=disk
cpu=CPU()
disk=Disk()
com=Computer(cpu,disk)
#类对象的浅拷贝
import copy
com2=copy.deepcopy(com)
print(com,'子对象的内存地址：',com.cpu,com.disk)
print(com2,'子对象的内存地址：',com2.cpu,com2.disk)