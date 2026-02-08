salary = int(input("enter your salary:"))
if salary < 30000:
    tax=5
elif 30000 <= salary <= 70000:
    tax=15
else:
    tax=25

print("Final Tax :",tax)
  
  