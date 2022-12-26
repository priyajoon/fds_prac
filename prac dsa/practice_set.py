n=int(input("total students = "))
list=[]
for i in range(n):
    student=input("enter name of student = ")
    list.append(student)
print("Students are :-")
print(list)

#cricket
n_c=int(input("total students who play cricket = "))
crick=[]
for i in range(n_c):
    s_c=input("enter name of student = ")
    crick.append(s_c)
print("Students are :-")
print(crick)

#badminton
n_b=int(input("total students who play badminton = "))
badi=[]
for i in range(n_b):
    s_b=input("enter name of student = ")
    badi.append(s_b)
print("Students are :-")
print(badi)

#football
n_f=int(input("total students who play football = "))
foot=[]
for i in range(n_f):
    s_f=input("enter name of student = ")
    foot.append(s_f)
print("Students are :-")
print(foot)

#play both cricket and football
def play_both_and(list1,list2):
    both=[]
    n1=len(list1)
    n2=len(list2)
    
    for i in range(n1):
        for j in range(n2):
            if list1[i]==list2[j]:
                both.append(list1[i])
    return both
print("students who play both cricket and badminton are")
print(play_both_and(crick,badi))

#play either cricket or badminton not both
def cnot_both(cricket,badminton):
    only_cri = []
    for i in range(n_c):
        flag = 0
        for j in range(n_b):
            if cricket[i] == badminton[j]:
                flag = 1
        if flag == 0:
            only_cri.append(cricket[i])


    only_bad = []
    for i in range(n_b):
        flag = 0
        for j in range(n_c):
            if cricket[j] == badminton[i]:
                flag = 1
        if flag == 0:
            only_bad.append(badminton[i])
    fi_list=[]
    for i in only_cri:
        fi_list.append(i)
    for j in only_bad:
        fi_list.append(j)
    return fi_list
print("students who play either cricket or badminton not both")
print(cnot_both(crick,badi))

##number of students who neither play cricket nor badminton
def neither_nor(list1,list2):
    
    list5=[]
    for i in list2:
        list1.append(i)
        
    for i in range(n):
        flag=0
        for j in range(len(list1)):
            if list[i]==list1[j]:
                flag=1
        if flag==0:
            list5.append(list[i])
    return list5
    
print("number of student who play neither cricket nor badminton")
print(neither_nor(crick,badi))
        
#students who play cricket and football but not badminton
def both_but_not(list1,list2,list3):
    merge=play_both_and(list1,list3)
    res=[]
    for i in range(len(merge)):
        flag=0
        for j in range(len(list2)):
            if merge[i]==list2[j]:
                flag=1
        if flag==0:
            res.append(merge[i])
    return res
print("students who play cricket and football but not badminton")
print(both_but_not(crick,badi,foot))
            