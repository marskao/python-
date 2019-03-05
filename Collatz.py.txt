def collatz(number):
  while number !=1:
    if number %2 == 0:
      number = number//2
    else:
      number = 3*number + 1
    print(number)
try:
  spam = int(input())
  collatz(spam)
except ValueError:
  print("Please Input an Integer")