students={}
while True:
    print("A-Add a student")
    print("B-Update marks")
    print("C-Search for a student")
    print("D-Display all students and marks")
    ch=input("Enter choice:").upper()
    if ch == 'A':
        name=input("Student name:")
        marks=int(input("Marks:"))
        students[name]=marks
    elif ch == 'B':
        name=input("Student name:")
        if name in students:
            students[name]=int(input("New marks:"))
        else:
            print("student  not found")
    elif ch == 'C':
            print("Marks:",students.get(name,"student not found"))
    elif ch == 'D':
         for i,j in students.items():
              print(i,":",j)
else: 
    brea