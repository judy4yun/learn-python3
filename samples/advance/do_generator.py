#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

#杨辉三角
# (代码作者的id：风袭6729) 
def triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]
#通过观察杨辉三角可知，下一行的每一个元素都依次由本行中每两个相邻元素之和得到，这个方法可以用一个技巧实现，
#即：将本行list拷贝出两个副本，将两个副本错1位，然后加在一起。
#由于错位后，前后各多了一个元素，所以要在错位后的两个list的前后各加一个[0]来补齐（其实，这个0是理所当然的，是杨辉三角的一部分）。


#输出部分代码
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
