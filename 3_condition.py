age = 3
if age >= 18:
    print('adult')
elif age >= 12:
    print('teenager')
else:
    print('kid')

friends = ['apple']
if friends:
    print('I have %d friends'% len(friends))
else:
    print('no friends')

weight = float(input('input weight(kg):'))
height = float(input('input height(cm):')) / 100

bmi = weight/(height*height)

if bmi <= 18.5:
    message = '过轻'
elif bmi <= 25:
    message = '正常'
elif bmi <= 28:
    message = '过重'
elif bmi <= 32:
    message = '肥胖'
else:
    message = '严重肥胖'
print('BMI is %f，属于 %s'% (bmi, message))
