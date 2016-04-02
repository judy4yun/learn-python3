#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

class GraduateStudent(Student):
    pass

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 99
print('g.score =', g.score)

#第一，slots只能限制添加属性，不能限制通过添加方法来添加属性：
def set_city(self, city):
    self.city=city

class Student(object):
    __slots__ = ('name', 'age', 'set_city')
    pass

Student.set_city = MethodType(set_city, Student)

a = Student()
a.set_city(Beijing)
a.city
#Student类限制两个属性name 和 age，但可以通过添加方法添加一个city属性（甚至可以添加很多属性，只要set_city方法里有包括）


#第二，属性分实例属性和类属性，多个实例同时更改类属性，值是最后更改的一个

def set_age(self,age):
    self.age=age

class Stu(object):
    pass

s=Stu()
a=Stu()

from types import MethodType

Stu.set_age=MethodType(set_age,Stu)

a.set_age(15) \\通过set_age方法，设置的类属性age的值
s.set_age(11) \\也是设置类属性age的值，并把上个值覆盖掉
print(s.age,a.age) \\由于a和s自身没有age属性，所以打印的是类属性age的值

a.age = 10  \\给实例a添加一个属性age并赋值为10
s.age = 20  \\给实例b添加一个属性age并赋值为20
\\这两个分别是实例a和s自身的属性，仅仅是与类属性age同名，并没有任何关系

print(s.age,a.age)  \\打印的是a和s自身的age属性值，不是类age属性值

#所以， 1，slots并不能严格限制属性的添加，可通过在方法里定义限制之外的属性来添加本不能添加的属性（当然，前提是方法没有被限制） 
#2，类属性是公共属性，所有实例都可以引用的，前提是实例自身没有同名的属性，因此类属性不能随意更改（别的实例可能在引用类属性的值
#就是说不能随便用a.set_age()更改age的值（因为调用此方法更改的是类属性age的值，不是实例a自身的age属性值）
