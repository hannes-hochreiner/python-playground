def factorial(num):
  if num == 0:
    return 1
  else:
    return num * factorial(num - 1)

number = int(input("Please enter a number: "))
print(f"The factorial of {number} is {factorial(number)}")
