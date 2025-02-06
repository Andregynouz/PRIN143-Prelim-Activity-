Mich = [int(input("Enter a number: to be added or deleted: "))]

Mich3 = 

Mich2 = input("Would you like to Add or Del your number?")


    
def Add():
    global Mich
    global Mich3
    Mich3.append(Mich)
    print(Mich3)
    mich()

def Del():
    global Mich
    global Mich3
    if Mich in Mich3:
        Mich.remove(Mich)
        print(Mich3)
    else:
        print("Input Error")
        
def mich():
    global Mich
    global Mich2
    global Mich3
    Mich = int(input("Enter a number: to be added or deleted: "))
    Mich1 = ["Add","Del"]
    Mich2 = input("Would you like to Add or Del your number?")
    
    if Mich2 == "Add":
        Add()
        print(Mich3)
        mich()
    elif Mich2 == "Del":
        Del()
        print(Mich3)
        mich()

if Mich2 == "Add":
    Add()
    print(Mich3)
    mich()
elif Mich2 == "Del":
    Del()
    print(Mich3)
    mich()
