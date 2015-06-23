
first_name = "Minwoo"
last_name = "Kim"
phone = "82-111-1234"

stock = ('GOOG', 100, 490.10)
address = ('www.python.org', 80)
person = (first_name, last_name, phone)

print stock
print address
print person

stock = 'GOOG', 100, 490.1
address =  'www.python.org', 80
person = 'Minwoo', 'Kim', '+82-111-1234'

print stock
print address
print person

a = ()
b = ('item',)
c = 'item',
d = ('item')  # this is not tuple!!!

print a
print b
print c
print d



# note : 튜플의 내용은 변경할 수 없음.
# 단일 객체라고 보는 것이 적절
