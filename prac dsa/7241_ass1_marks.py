#Name = Priya
#Branch = Comp B
#Roll no. =7241
#batch = S5
#students
#marks of students


#enter details of student marks

n=int(input("Number of students in the class = "))
list=[]
print("If student is absent enter -1")
for i in range(n):

    marks=int(input("Enter marks of students = "))
    list.append(marks)
print(list)

#find average marks obtained
def average(list):
    total_marks = 0
    average_marks = 0
    count = 0
    for i in range(n):
        if list[i] != -1:
            total_marks += list[i]
            count += 1
    average_marks = total_marks / count
    return average_marks
print("Average marks = ",average(list))

#highest marks obtained
def highest_score(list):
    highest = list[0]
    for i in range(n):
        if list[i] > highest:
            highest = list[i]
    return highest

print("Highest marks obtained = ",highest_score(list))

#lowest marks obtained
def lowest_score(list):
    lowest = list[0]
    for i in range(n):
        if list[i] != -1:
            if list[i] < lowest:
                lowest = list[i]
    return lowest
print("Lowest marks obtained = ",lowest_score(list))

def absent(list):
    count1 = 0
    for i in range(n):
        if list[i] == -1:
            count1 += 1
    return count1
print("Number of absent students = ",absent(list))

#frequency of marks
def freq(list):
    frequency = []
    for i in range(0, 101):
        frequency.append(0)
    for i in range(0, n):
        element = list[i]
        if element != -1:
            frequency[element] += 1
    mode = []
    mark = 0
    for i in range(0, 101):
        if frequency[i] > mark:
            mark = frequency[i]
    for i in range(0, 101):
        if frequency[i] == mark:
            mode.append(i)
    return mode
print("Marks with Highest Frequency: ", freq(list))

#percentage of pass and fail students
def passed(list):
    pas=0
    fail=0
    abs=0
    for i in range(0,n):
        if list[i]>=40:
            pas+=1
        elif(list[i]!=-1):
            fail+=1
        else:
            abs+=1
    print("Percentage of students passed who appeared: ",(pas/(n-abs))*100)
    print("Percentage of students failed who appeared: ",(fail/(n-abs))*100)
passed(list)


#top three marks
def top_three_std(list):

    for i in range(0,n):
        for j in range(0, n):
            if list[j] > list[i]:
                list[i], list[j] = list[j], list[i]

    if(n<3):
        print("There are less than 3 students")
    else:
        print("Top 3 Highest Scores: ",list[n-1],list[n-2],list[n-3])
top_three_std(list)



