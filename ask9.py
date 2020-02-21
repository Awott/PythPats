def sd(x):
    s=0
    while(x>0):
       d=x%10
       s=s+d
       x=x//10
    return s   


n= int(input("enter your value: "))
while (n >= 10):
    n = 3*n+1
    n = sd(n)
    #print(n)    


     
