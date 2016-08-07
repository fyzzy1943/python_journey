friends = ['apple', 'banana', 'orange']

print(friends)

print(len(friends))

friends.insert(50, 'pear')
print(friends)

friends.insert(10, 'cherry')
print(friends)

print(friends.insert(-10, 'peach'))
print(friends)

print(friends[-1])

print(friends.pop(-6))
print(friends)

friends.append(0xA)
print(friends.append(0o11))
print(friends)

friends[-1] = 3
print(friends)

friends[1] = ['great', 'good', 'better']
print(friends)

print(friends[1], friends[1][0])
friends[1][0] = True
friends[1][1] = None
print(friends)

peoples = (1, 2, False)
print(peoples)

people = ()
print(people)

# peoples[1] = 1
# print(peoples)

friends.append('世界')
print(friends)

# the work
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

L.append('Tiger')
print(L)

L[0][0] = ('Einstein', 'Maxwell')
print(L)
print(0)
