#SECOND REPRESENTATION (2-D List)"


##first polynomial
n = int(input("Enter number of terms in first polynomial: "))
N = int(input("Enter highest degree: "))
lis_1 = []
for i in range(0, n):
    x = int(input("Enter power = "))
    y = int(input("Enter coefficient:= "))
    lis = []
    lis.append(y)
    lis.append(x)
    lis_1.append(lis)
print(lis_1)

m = int(input("Enter number of terms in second polynomial: "))
M = int(input("Enter highest degree: ="))
lis_2 = []
for i in range(0, m):
    x = int(input("Enter power = "))
    y = int(input("Enter coefficient = "))
    lis = []
    lis.append(y)
    lis.append(x)
    lis_2.append(lis)


def display1(lis):
    n = len(lis)
    for i in range(0, n):
        x = lis[i][0]
        if x == 0:
            continue
        s = ""
        if (x > 0):
            s = "+"
        else:
            s = "-"
        print(s + str(x) + " X^" + str(lis[i][1]), end=' ')
    print("")

def addition1(lis1, lis2):
    n = len(lis1)
    m = len(lis2)
    i = 0
    j = 0
    lis = []
    while (i + j < n + m):
        if (i == n):
            lis.append(lis2[j])
            j += 1
        elif (j == m):
            lis.append(lis1[i])
            i += 1
        else:
            x = lis1[i][1]
            y = lis2[j][1]
            if (x > y):
                lis.append(lis1[i])
                i += 1
            elif (y > x):
                lis.append(lis2[j])
                j += 1
            else:
                lis3 = []
                lis3.append(lis1[i][0] + lis2[j][0])
                lis3.append(x)
                lis.append(lis3)
                i += 1
                j += 1
    return lis


def multiplication1(lis1, lis2):
    n = len(lis1)
    m = len(lis2)
    lis = []
    N = lis1[0][1]
    M = lis2[0][1]
    for i in range(N + M + 1):
        lis.append(0)
    for i in range(0, n):
        for j in range(0, m):
            lis[lis1[i][1] + lis2[j][1]] += (lis1[i][0] * lis2[j][0])
    return lis

def evaluate1(lis, k):
    ans = 0
    n = len(lis)
    for i in range(0, n):
        x = lis[i][0]
        y = lis[i][1]
        z = k ** y
        ans += (x * z)
    return ans
def display(lis):
    n=len(lis)
    for i in range(n-1,-1,-1):
        x=lis[i]
        if x==0:
            continue
        s=""
        if(x>0):
            s="+"
        else:
            s="-"
        print(s+str(x)+" X^"+str(i), end=' ')
    print("")

display1(lis_1)
display1(lis_2)
A_lis=addition1(lis_1, lis_2)
B_lis=multiplication1(lis_1, lis_2)
print("ADDITION IS : ")
display1(A_lis)
print("MULTIPLICATION IS: ")
display(B_lis)
x=int(input("Give value for x "))
y=evaluate1(lis_1, x)
z=evaluate1(lis_2, x)
print("Value for the first polynomial for the given x is: " + str(y))
print("Value for the second polynomial for the given x is: " + str(z))

