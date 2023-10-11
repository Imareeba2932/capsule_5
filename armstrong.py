i=int(input('enter the number:'))
orig=i
sum=0
while(i>0):
    sum=sum+(i%10)**3
    i=i//10
if sum==orig:
    print('Armstrong number')
else:
    print('Not an armstrong number')