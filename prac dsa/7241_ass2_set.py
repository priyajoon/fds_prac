#set
#Name = Priya
#Branch = Comp B
#Roll no. =7241
#batch = S5
#

n=int(input("Total students = "))
student=[]
print("enter roll no ")
for i in range(n):
    s=input()
    student.append(s)
print("students are= ", student)


n_c=int(input("number of students who play cricket = "))
print("enter roll no ")
cricket=[]
for i in range(n_c):
    c=input()
    if c not in cricket:
        cricket.append(c)

print("students who play cricket")
print(cricket)

n_b=int(input("number of students who play badminton = "))
print("enter roll no ")
badminton=[]
for i in range(n_b):
    b=input()
    if b not in badminton:
        badminton.append(b)
print("students who play badminton = ", badminton)


n_f=int(input("number of students who play football = "))
print("enter roll no ")
football=[]
for i in range(n_f):
    f=input()
    if f not in football:
        football.append(f)
print("students who play football = ", football)


#play both cricket and badminton
def crick_bad(cricket,badminton):
    both_candb = []
    for i in range(n_c):
        for j in range(n_b):
            if cricket[i] == badminton[j]:
                both_candb.append(cricket[i])
 #   return both_candb
#print("Students who play both cricket and badminton are ", crick_bad(cricket, badminton))

def cr_bad(cricket,badminton):
    both_c_b=[]
    for i in cricket:
        if i in badminton:
            both_c_b.append(i)
    return both_c_b
print("Students who play both cricket and badminton are ", cr_bad(cricket, badminton))


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
print("students who play cricket or badminton but not both = ",cnot_both(cricket, badminton))





#number of students who neither play cricket nor badminton
def neither_c_b(cricket,badminton):
    crik_bad = []
    for i in range(n_c):
        crik_bad.append(cricket[i])
    for i in range(n_b):
        flag = 0
        for j in range(n_c):
            if badminton[i] == crik_bad[j]:
                flag = 1
        if flag == 0:
            crik_bad.append(badminton[i])
    #print("student who play both crick and badminton")
    #print(crik_bad)
    neither = []
    for i in range(n):
        flag = 0
        for j in range(len(crik_bad)):
            if student[i] == crik_bad[j]:
                flag = 1
        if flag == 0:
            neither.append(student[i])
    return len(neither)
    #print("number of student who play neither cricket nor badminton", len(neither))
    #print(neither)
print("number of student who play neither cricket nor badminton", neither_c_b(cricket,badminton))

#students who play cricket and football but not badminton

def cr_foot_bad(cricket,badminton,football):
    crik_foot = []
    for i in range(n_c):
        crik_foot.append(cricket[i])
    for i in range(n_f):
        flag = 0
        for j in range(n_c):
            if football[i] == crik_foot[j]:
                flag = 1
        if flag == 0:
            crik_foot.append(football[i])
    ##print("students who play both cricket and football")
    #print(crik_foot)

    not_bad = []
    for i in range(len(crik_foot)):
        flag = 0
        for j in range(n_b):
            if crik_foot[i] == badminton[j]:
                flag = 1
        if flag == 0:
            not_bad.append(crik_foot[i])
    return len(not_bad),not_bad

    #print("number of students who play both criket and football nor badminton = ", len(not_bad))
    #print(not_bad)
print("number of students who play both criket and football nor badminton = ", cr_foot_bad(cricket, badminton, football))

## students playing at least one game
def at_least_one(crick,bad,foot,std) :
    ans = []
    for i in std :
        if i in crick or i in bad or i in foot :
            ans.append(i)
    return ans

print('students playing at least one game : ',at_least_one(cricket,badminton,football,student))

# students playing all three games games
def all_games(cricket,badminton,football):
    all=[]
    for i in cr_bad(cricket,badminton):
        if i in football:
            all.append(i)
    return all
print('students playing all three games games : ', all_games(cricket,badminton,football))

#number of students not playing any game
print("number of students not playing any game : ", n - len(at_least_one(cricket,badminton,football,student)))
