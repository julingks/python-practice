a = "Hello World"
b = 'Python is groovy'
c = """Computer says 'No'"""

print a, b, c

print '''Content-type: text/html

<h1> Hello World</h1>
Click <a href="http://www.python.org">here</a>
'''
print a[0],a[1],a[2]

# a = "Hello World"
print a[:5]  # Hello
print a[6:]  # World
print a[3:8] # lo Wo

x = "12"
y = "34"
z = x + y
print z  # 1234

z = int(x) + int(y)
print z  # 46

n = 3.4
print str(n)  # 3.4
print repr(n) # 3.4?
