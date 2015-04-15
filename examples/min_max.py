import sys
if len(sys.argv) != 2 :
	print "Please supply a filenmae"
	raise SystemExit(1)
f = open(sys.argv[1])
lines = f.readlines()
f.close()

# list comprehension
fvalues = [float(line) for line in lines]

print "The minimum value is ", min(fvalues)
print "The maximum value is ", max(fvalues)

