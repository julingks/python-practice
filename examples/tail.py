#!/usr/bin/python
# _*_ coding: utf-8 _*_

import time
def tail(f):
	f.seek(0, 2)  # 파일 끝으로 이동
	while True:
		line = f.readline()  # 다음 줄 읽기를 시도
		if not line:		 # 아무것도 없으면 잠시 쉬었다가 다시 시도
			time.sleep(0.1)
			continue
		yield line

def grep(lines, searchtext):
	for line in lines:
		if searchtext in line: yield line

# 유닉스 "tail -f | grep python"의 구현
wwwlog = tail(open("resources/tail.txt"))
pylines = grep(wwwlog, "python")

for line in pylines:
	print line,

