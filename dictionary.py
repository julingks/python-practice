#!/usr/bin/python
# -*- coding: utf-8 -*-
# 인코딩 설정

# empty dictionary
pirces = {}
prices = dict()

prices = {
	"GOOG" : 490.10,
	"AAPL" : 123.50,
	"IBM" : 91.50,
	"MSFT" : 52.13
}

if "GOOG" in prices:
	p = prices["GOOG"]
else:
	p = 123

print p

# prices.get( key, default)
print prices.get("SCOX", 0.0)  # 0.0

syms = list(prices)
print syms

# 사전에서 요소 삭제
del prices['MSFT']
print prices

