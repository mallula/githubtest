with open('file2.txt','w') as fp1
fp1.write('Hello')
fp1.close
fp1=fp1=open('file2.txt','r')
fp2=open('fptest.txt','r')
str1=''
str2=''
for x in fp1:
    str1+=x
for y in fp2:
    str2+=y
print(str1)
print(str2)

if str1==str2:
    print('same')
else:
    print('no')
fp1.seek(0)
fp2.seek(0)
print(fp1.read())
print(fp2.read())

