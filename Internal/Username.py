username = input("enter username: ")
password = input("enter password: ")
if(username == "admin" and password == "pass"):
   print("LOGIN Successful!")
elif(username != "admin"):
   print("Wrong username")
else:
   print("wrong password")      