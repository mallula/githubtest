fp = open('fptest.txt', mode='r')
x = fp.read()
str1 = ''
for n in x:
    str1 += n
if str1 == 'Hello':
    print("yes")
else:
    print('no')

fp.close
