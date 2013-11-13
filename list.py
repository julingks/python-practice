# list 

names = [ "Dave", "Mark", "Ann", "Phil" ]

print names[2] # Ann
names[0] = "Jeff" # start with 0 index!

print names # ['Jeff', 'Mark', 'Ann', 'Phil']
names.append("Paula")
names.insert(2,"Thomas")

print names 
#     0       1        2       3      4         5
# ['Jeff', 'Mark', 'Thomas', 'Ann', 'Phil', 'Paula']

print names[2:3]  # ['Thomas']
print names[2:4]  # ['Thomas', 'Ann']
print names[0:2]  # ['Jeff', 'Mark']

a = [1,2,3] + [4,5]
print a  # [1, 2, 3, 4, 5]

# empty list
names = []
names = list()

# nested list
a = [1, "Dave", 3.14, ["Mark", 7, 9, [100,101]], 10]


