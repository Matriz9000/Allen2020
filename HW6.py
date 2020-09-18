a = int(input("choose a fucking number man"))
b = int(input("choose a fucking number man"))
factors = []
small=0
g=0
if a>b:
    small=b
else:
    small=a
for i in range(1,small+1):
    if ((a % i == 0) and (b % i == 0)):
       g = i
print((g*(a/g))*(b/g))


