#user input
x = input("Enter your first number: ")
y = input("Enter your second number: ")

#storing the input as integers
num1 = int(x)
num2 = int(y)

#finding the sum, difference, product, and quotient
sum = num1 + num2
product = num1 * num2
difference = num1 - num2
quotient = num1 / num2

#using If-Else Statement to check is the second number is 0
if (num2 == 0):
  print("Second number cannot be 0, please try again.")
else:
  print(f"The sum of {x} and {y} is {sum}")
  print(f"The difference of {x} and {y} is {difference}")
  print(f"The product of {x} and {y} is {product}")
  print(f"The quotient of {x} and {y} is {quotient}")