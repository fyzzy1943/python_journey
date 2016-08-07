print('中文str')

print(ord('啊'))
print(chr(65))
print(chr(21834))

print('\u5538\u00dd')

print(b'133aas\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print('b\'133aas\'')
print('有趣'.encode())

print(len('中文'))
print(len('中文'.encode()))

print('%04d' % 100)
print('%s is a %s%%%10s'% ('einstein', 'nice', 'student'))
print('%.3s'% ('hello!'))

print('中文'.encode('gb2312'))
print('中文'.encode('utf-8'))
print('''
    it's
funny
''')
print('py里居然没有!..')
print(not True)

# practice
s1 = 72
s2 = 85
print('相比去年提升%.1f%%'% ((s2-s1)/s1*100))
