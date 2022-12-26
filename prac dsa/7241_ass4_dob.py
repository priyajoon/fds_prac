#It is decided that weekly greetings are to be furnished to wish the students having their birthdays in that week.
# The consolidated sorted list with desired categorical information is to be provided to the authority.
# Write a Python program to store students PRNs with date and month of birth. Let List_A and List_B be the two list
# for two SE Computer divisions. Lists are sorted on date and month. Merge these two lists into third list “List_SE_Comp_DOB”
# resulting in sorted information about Date of Birth of SE Computer students


#Name = Priya
#Branch = Comp B
#Roll no. =7241
#batch = S5


#enter data for comp a
n=int(input("enter the number of students in comp A = "))
comp_A=[]
for i in range(n):
    print("student ", i + 1)
    std=[]
    prn=int(input("enter prn no. = "))
    std.append(prn)
    date=input("enter date of birth = ")
    std.append(date)
    month=int(input("enter month = "))
    std.append(month)
    comp_A.append(std)
print(comp_A)

#enter data for comp b
m=int(input("enter the number of students comp B= "))
comp_B=[]
for i in range(m):
    print("student ", i+1)
    std=[]
    prn=int(input("enter prn no. = "))
    std.append(prn)
    date=input("enter date of birth = ")
    std.append(date)
    month=int(input("enter month = "))
    std.append(month)
    comp_B.append(std)
print(comp_B)

#sorting and merging data of both divisions
def sorted(c_a, c_b):
    merge_s = []
    n = len(c_a)
    m = len(c_b)
    i1 = 0
    i2 = 0
    while (i1 < n and i2 < m):
        if (c_a[i1][2] < c_b[i2][2]):
            merge_s.append(c_a[i1])
            i1 = i1+1
        elif (c_a[i1][2] > c_b[i2][2]):
            merge_s.append(c_b[i2])
            i2 = i2+1
        elif (c_a[i1][2] == c_b[i2][2]):
            if (c_a[i1][1] < c_b[i2][1]):
                merge_s.append(c_a[i1])
                i1 = i1+1
            elif (c_a[i1][1] > c_b[i2][1]):
                merge_s.append(c_b[i2])
                i2 = i2+1
            else:
                merge_s.append(c_a[i1])
                i1 = i1+1
                merge_s.append(c_b[i2])
                i2 = i2+1
    while (i1 < n):
        merge_s.append(c_a[i1])
        i1 = i1+1

    while (i2 < m):
        merge_s.append(c_b[i2])
        i2 = i2+1
    return merge_s

print("merging data of both divisions")
print(sorted(comp_A,comp_B))