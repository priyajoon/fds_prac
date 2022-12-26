#polynomial by first method

m=int(input("no. of terms in polynomila A = "))
n=int(input("no. of terms in polynomila B = "))
da=int(input("heighst degree of A = "))
db=int(input("heighst degree of B = "))


print("polynomial A")
a=[0 for i in range(da+1)]
for j in range(m):

    coef=int(input("enter coefficient = "))
    exp=int(input("enter exponent = "))
    a[exp]=coef

for j in range(da+1):
    print(a[j], end=" ")
print()
for i in range(da+1):
    if a[i]==0:
        continue
    else:
        print(a[i],"xe",i,"+",end=" ")
print()


print("polynomial B")
b=[0 for i in range(db+1)]
for j in range(n):

    coef = int(input("enter coefficient = "))
    exp = int(input("enter exponent = "))
    b[exp] = coef

for j in range(db + 1):
    print(b[j], end=" ")
print()
for i in range(db+1):
    if b[i]==0:
        continue
    else:
        print(b[i],"xe",i,"+",end=" ")
print()

#addition of polynomial
result=[]
x=int
y=int
if da>=db:
    x=da
    y=db
else:
    x=db
    y=da

result=[0 for i in range(x+1)]
for i in range(y+1):
    result[i]=a[i]+b[i]


for i in range(y+1,x+1):

     if da > db:
         result[i] = a[i]
     else:
         result[i] = b[i]

print("addition of polynomial")
for i in range(x+1):
    print(result[i], end=" ")
print()
for i in range(x+1):
    if result[i]==0:
        continue
    else:
        print(result[i],"xe",i,"+",end=" ")
print()

#multiplication of polynomial
multi=[0 for i in range(da+db+1)]
for i in range(da+1):
    for j in range(db+1):
        multi[i+j]+=a[i]*b[j]
print("multiplication of polynomial")
for i in range(da+db+1):
    print(multi[i],end=" ")
print()

#representation

for i in range(da+db+1):
    if multi[i]==0:
        continue
    else:
        print(multi[i],"xe",i,"+",end=" ")
print()

#find at x
x = int(input("enter the value of x "))

ev = 0
for i in range(0, len(multi)):
    ev = ev + multi[i] * (x ** i)
print("value of product of two polynomials at " + str(x) + " is ")
print(ev)

ea = 0
for i in range(0, len(result)):
     ea = ea + result[i] * (x ** i)
print("value of addition of two polynomials at " + str(x) + " is ")
print(ea)
