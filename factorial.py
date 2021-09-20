def factorial(num):
  return 1 if num == 0 else num * factorial(num-1)

if __name__ == '__main__':
  number = int(input("Please enter a number: "))
  print(f"The factorial of {number} is {factorial(number)}")
