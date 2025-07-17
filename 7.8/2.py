class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f'我叫{self.name},我今年{self.age}岁了')

stu1=Student('ysj',10)
stu2=Student('xyz',20)
stu3=Student('ada',21)
print(type(stu1))
print(type(stu2))
print(type(stu3))
lst=[stu1,stu2,stu3]
stu2.gender='男'
print(stu2.gender)