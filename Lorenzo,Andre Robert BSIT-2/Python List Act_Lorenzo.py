one = input ("Enter The Name of the Book: ")
Title = []
one1 = input ("Would you like to Add or Delete your input? ")

def Add_Title():
    global Title
    global one
    Title.append(one)
    print(Title)
    Title1()

def Del_Title():
    global Title
    global one
    one2 = input("What book would you like to delete? ")
    if one2 in Title:
        Title.remove(one2)
        print(Title)
        Title1()
    else:
        print("Input Error")
        Title1()

def Title1():
    global Title
    global one
    global one1
    one = input ("Enter The Name of the Book: ")
    one1 = input ("Would you like to Add or Delete your input? ")

    if one1 == "Add":
        Add_Title()
    elif one1 == "Delete":
        Del_Title()
    else:
        print("Input Error")

if one1 == "Add":
    Add_Title()
elif one1 == "Delete":
    Del_Title()
else:
    print("Input Error")
    
