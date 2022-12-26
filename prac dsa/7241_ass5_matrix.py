#matrix 1
#Name = Priya
#Branch = Comp B
#Roll no. =7241
#batch = S5
print("first matrix")
r = int(input("number of rows = "))
c = int (input("number of columns = "))
print("enter matrix elements")
matrix=[]
for i in range(r):
    a=[]
    for j in range(c):
        val=int(input())
        a.append(val)
    matrix.append(a)

for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()

print("checking if matrix is upper triangular or not")
#upper triangle
flag=1
for i in range(0,r):
    for j in range(0,i):
        if matrix[i][j]!=0:
            flag=0
if flag==1:
    print("the matrix is upper triangular matrix")
else:
    print("the matrix is not upper triangular matrix")

# transpose
# res=[[0 for i in range(r)] for j in range(c)]
print("transpose of matrix is ")
x=len(matrix)
y=len(matrix[0])
trans = [[0 for i in range(y)] for j in range(x)]


for i in range(y):
    for j in range(x):
        trans[i][j] = matrix[j][i]

for i in range(y):
    for j in range(x):
        print(trans[i][j], end=" ")
    print()
#summation of diagonal elements
print("finding summation of diagonal elements")
sum=0
sum_s=0
if r!=c:
    print("matrix is not square matrix")
else:
    for i in range(r):
        for j in range(c):
            if i==j:
                sum+=matrix[i][j]
            if (i+j)==r-1:
                sum_s+=matrix[i][j]

    print("sum of principal diagonal = ",sum)
    print("sum of secondary diagonal = ",sum_s)

print("second matrix")
#matrix2
r2 = int(input("number of rows = "))
c2 = int(input("number of columns = "))
print("enter elements of second matrix")
matrix2 = []
for i in range(r2):
    a2 = []
    for j in range(c2):
        val2 = int(input())
        a2.append(val2)
    matrix2.append(a2)

for i in range(r2):
    for j in range(c2):
        print(matrix2[i][j], end=" ")
    print()


#addition
print("addition of matrix 1 and 2")
result=[]
if r==r2 and c==c2:
    for i in range(0,r):
        result.append([])
        for j in range(0,c):
            result[i].append(matrix[i][j]+matrix2[i][j])

    for i in range(r):
        for j in range(c):
            print(result[i][j], end=" ")
        print()
else:
    print("the matrix cannot be added")


#multiplication
print("multiplying both matrices")
result=[[0 for i in range(r)] for j in range(c2)]
if r2!=c:
    print("multiplication not possible")

else:
    for i in range(0, r):
        for j in range(0, c2):
            result[i][j] = 0
            for k in range(0, r2):
                result[i][j] += matrix[i][k] * matrix2[k][j]
print("multiplication of two matrices")
for r in result:
    print(r)



print("find saddle point")
#saddle point
ans=0
flag=0
n=len(matrix)
m=len(matrix[0])
k=0
c_index=0
for i in range(n):
    min_r=matrix[i][0]
    c_index=0
    for j in range(m):
        if min_r>matrix[i][j]:
            min_r=matrix[i][j]
            c_index=j
            x1=i
            y1=j


    k=0
    for k in range(n):
        if min_r<matrix[k][c_index]:
            min_r=matrix[k][c_index]
            break
        k+=1

    if k==n:
        flag=1
        ans=min_r

if flag==1:
    print("saddle point is =", ans)
    print("saddle point is present at = ",k+1," ",c_index+1)

else:
    print("no saddle point")


print("check if magic square or not")
#magic square
if r!=c:
    print("not magic square matrix")
else:
    #check row
    check_row=[]
    sum=0
    for i in range(r):
        sum=0
        for j in range(r):
            sum+=matrix[i][j]
        check_row.append(sum)

    for i in range(r):
        if check_row[i]!=check_row[0]:
            print("not square matrix")
            break



    #column
    sum_col=0
    for i in range(r):
        sum_col=0
        for j in range(r):
            sum_col+=matrix[j][i]
    # diagonal
    sum_diag = 0
    for i in range(r):
        for j in range(c):
            if i == j:
                sum_diag += matrix[i][j]
    print("addition of diagonal matrix",sum_diag)
    print("addition of row", sum)
    print("addition of columns", sum_col)

    k=sum
    k1=sum_col
    k2=sum_diag
    if k==k1==k2:
        print("yes it is magic square matrix")
    else:
        print("no it is not a magic square matrix")




