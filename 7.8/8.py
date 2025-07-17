class FatherA():
    def __init__(self,name):
        self.name=name

    def showA(self):
        print('父类A中的方法')

class FatherB():
    def __init__(self, age):
        self.age=age

    def showb(self):
        print('父类B中的方法')

# 多继承
class Son(FatherA, FatherB):
    def __init__(self, name, age, gender):
# 需要调用两个父类的初始化方法
        FatherA.__init__(self, name)
        FatherB.__init__(self,age)
        self.gender=gender
    def showA(self):
        FatherA.showA(self)
        print('这是单独的方法重写的结果')

son=Son('惠子洲',19,'男')#调用Son类中的 __ init __ 执行
son. showA()

