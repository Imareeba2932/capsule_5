i=int(input("Enter a number: "))
orig=i
pal = 0
while(i>0):
    pal = pal*10+(i%10)
    i=i//10
if(orig==pal):
    print("Pallindrome")
else:
    print("Not Pallindrome")