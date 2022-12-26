#Name = Priya
#Branch = Comp B
#Roll no. =7241
#batch = S5
#library

#enter book name and price
n=int(input("number of books = "))
book=[]
print("enter name of book and price")
for i in range(n):
    s=[]

    name=input("name : ")
    price=int(input("price : "))
    s.append(name)
    s.append(price)
    book.append(s)

print("books available in library ")
print(book)

#duplicate entries
def copy(book):
    new_book=[]
    for i in book:
        if i not in new_book:
            new_book.append(i)

    return new_book
print("Removing duplicate copies ", copy(book))

#arranging in ascending order on basis of cost
def sort(book):
    #arranging in ascending order on basis of cost
    for i in range(len(book)):
        for j in range(len(book)):
            if book[i][1] < book[j][1]:
                book[i][1], book[j][1] = book[j][1], book[i][1]
    return book
print("arranging books in ascending order of their cost", sort(book))



#number of books cost greater than 500
def cost(book):
    count = 0
    for i in range(len(book)):
        if book[i][1] > 500:
            count +=1
    return count
print("count number of books having price greater than 500 = ",cost(book))

#books having cost less than 500
def less(book):
    new_list = []
    for i in range(len(book)):

        if book[i][1] < 500:
            new_list.append(book[i])
    return new_list
print("books having price less than 500", less(book))




