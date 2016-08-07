s1 = {1, 2, ('a', 'b'), True, '啊'}
print(s1)

d1={'einstein':95,'faraday':103}
print(d1)
print(d1['faraday'])
print(d1['einstein'])

d1['edison'] = 97
print(d1)

d1['maxwell'] = None
print(d1)

d1[True] = True
print(d1)

d1[1] = False
print(d1)

d1[(1,)] = (1,)
print(d1)

print('啊' in s1)
print(d1.items())
