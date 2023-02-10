def getdata():
    print("Enter your details\n")
    list1=[]
    for var in range(3):
        name = input("Enter your name: ") # string
        age = int(input("Enter your age: "))  # integer
        salary = float(input("Enter your salary: ")) # float
        list1.append([name,age,salary])
    print(list1)
    display(list1)
def display(LIST1):
    for i in range(3):
        print("Hello ",LIST1[i][0]," as your age is ",LIST1[i][1]," and your salary is ",LIST1[i][2]," so we offer you the loan.")
getdata()
