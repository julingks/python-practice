friends = ['john', 'pat', 'gray', 'michael']
for i, name in enumerate(friends):
    print "iteration {iteration} is {name}".format(iteration=i, name=name)
for name in friends:
    print "{name}".format(name=name)
