fruits = ('apple', b'banana'.decode())
for fruit in fruits:
    print(fruit)

sum = 0
for x in range(101):
    sum = sum + x

print(range(5), sum)

sum = 0
n = 1
while n <= 100:
    sum = sum + n
    n = n + 1
print(sum)

L = ['einstein', 'maxwell', 'tesla', 'faraday']
for future in L:
    print('hello, %s' % future, end=';')
