def sd(x):
    s=0
    while(x>0):
       dig=x%10
       s=s+dig
       x=x//10
    return s


n = int(input ("Enter your credit card number: "))
i = 1
n2 = n
lin = list(map(int,str(n)))
while (i < 17):
    if (i % 2 == 0 ):
        di = (int(lin[16-i]))*2
        if ( di > 9):
            di = sd(di)
        lin[16-i] = di      
    i = i + 1
ln = ''.join(map(str,lin))
sl = sd((int(ln)))
cv = sl % 10
if cv == 0 :
    print("This is a valid card")
else:
   print("This is not a valid card")
