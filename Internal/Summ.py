num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
if num2 !=0:
    quotient = num1/num2
else:
    quotient = "Undefined(division by zero)"
print("sum:",sum_result)
print("difference:",difference)
print("product:",product)
print("Quotient:",quotient)