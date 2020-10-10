
s = 1
for n in range(2,11):
    fact = 1
    for i in range(1,n+1): 
        fact = fact * i 
    s = s + fact
print (s)

