# -*- coding:utf8 -*-

# 二进制运算符测试
def bitwise():
    for i in range(0,2):
        for j in range(0,2):
            print(i,'&',j,'->',i&j)
    print('------------------------------')
    for i in range(0,2):
        for j in range(0,2):
            print(i,'|',j,'->',i|j)
    print('------------------------------')
    for i in range(0,2):
        for j in range(0,2):
            print(i,'^',j,'->',i^j)
    print('------------------------------')
    for i in range(0,2):
        print('~',i,'->',~i)

# 面向过程编程就是把计算机程序当作一系列指令的集合
# 面向对象编程就是把计算机程序当作一系列对象的集合
# 面向对象编程3大特性 封装 继承 多态
class Student(object):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print('my name is %s, my age is %d.' % (self.name, self.age)) 






if __name__ == '__main__':
    bitwise()
