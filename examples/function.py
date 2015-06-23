#!/usr/bin/python
# _*_ coding:utf-8 _*_


def remainder(a, b):
    # //는 끝수를 버리는 나누기
    q = a // b
    r = a - q*b
    return r


def divide(a, b):
    q = a // b
    r = a - q * b
    return (q, r)


# 7
print remainder(36, 15)
# (2, 7)
print divide(37, 15)

quotient, remainder = divide(37, 15)
