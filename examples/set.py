
s = set([3,5,9,9,10,10])
t = set('Hello')

print s # set([9, 10, 3, 5])
print t # set(['H', 'e', 'l', 'o'])

s.add('X')
s.update([1,2,3,4,5,6])

t.remove('H')

print s # set([1, 2, 3, 4, 5, 6, 9, 10, 'X'])
print t # set(['e', 'l', 'o'])
