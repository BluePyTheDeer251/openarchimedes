print("Welcome to my calculator app (codename: archimedes)")

#The calculator
def process():
  calculating_type = input("What do you want to calculate? Addition(1), Subtraction(2), Multiplication(3), or Division?(4) ")
  if calculating_type == 1:
      part1 = input("First number: ")
      part2 = input("Second number: ")
      result = int(part1) + int(part2)
      print("Result: " + result)
  if calculating_type == 2:
      part1 = input("First number: ")
      part2 = input("Second number: ")
      result = int(part1) - int(part2)
      print("Result: " + result)
  if calculating_type == 3:
      part1 = input("First number: ")
      part2 = input("Second number: ")
      result = int(part1) * int(part2)
      print("Result: " + result)

  if calculating_type == 4:
      part1 = input("First number: ")
      part2 = input("Second number: ")
      result = int(part1) / int(part2)
      print("Result: " + result)

print("I am pretty basic.")


