#Advanced Calculator lqdm12 basic.py
#I take as a string all of your calculation
string_calculate = input("Write your calculation: ")
num1 = ''
num2 = ''
op = ''

#With this operation I'm going to separate the first number, the operator sign and the second number in three different variables
for i in range(len(string_calculate)):
  if string_calculate[i] == '+' or string_calculate[i] == '-' or string_calculate[i] == '*' or string_calculate[i] == '/':
    op = string_calculate[i]
  else:
    if op == '':
      num1 += string_calculate[i]
    else:
      num2 += string_calculate[i]

if op == "+":
  print(float(num1) + float(num2))
elif op == "-":
  print(float(num1) - float(num2))
elif op == "*":
  print(float(num1) * float(num2))
elif op == "/":
  #Here I try to catch the error, because when every program has a division by zero will crash (math says it's impossible to calculate)
  try:
    print(float(num1) / float(num2))
  except ZeroDivisionError:
    print("You can't divide by zero")
else:
  print("Invalid operator")












