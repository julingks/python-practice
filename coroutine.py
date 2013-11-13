#!/usr/bin/python
# _*_ coding:utf-8 _*_

def print_matches(matchtext):
	print "Looking for", matchtext
	while True:
		line = (yield) # next()가 호출되면 여기까지 진행된다. 그 다음은 send()를 호출하면 진행
		if matchtext in line:
			print line
	
matchers = [
	print_matches("python"),
	print_matches("guido"),
	print_matches("jython"),
]

for m in matchers : m.next() # 모든 matcher를 준비시킨다

wwwlog = ["python asdfasdf","guido sdfasdf","asdfasdf jython"]

for line in wwwlog:
	for m in matchers:
		m.send(line)



	

