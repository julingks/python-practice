#!/usr/bin/python
# _*_ coding:utf-8 _*_


def remainder(a,b):
    q = a // b   # //는 끝수를 버리는 나누기
    r = a - q*b
    return r

def divide(a,b):
    q = a // b
    r = a- q*b
    return (q, r)


print remainder(36, 15)  # 7
print divide(37, 15) # (2, 7)

quotient, remainder = divide(37, 15)


