def add(a,b):
  answer = a + b
  print(str(a) + " + " + str(b) + " = " + str(answer)+ "\n")

def sub(a,b):
  answer = a - b
  print(str(a) + " - " + str(b) + " = " + str(answer)+ "\n")

def multiply(a,b):
  answer = a * b
  print(str(a) + " * " + str(b) + " = " + str(answer)+ "\n")

def div(a,b):
  answer = a / b
  print(str(a) + " / " + str(b) + " = " + str(answer)+ "\n")

while True:
  print(" A) Addition")
  print(" B) Subtraction")
  print(" C) Multiplication")
  print(" D) Division")
  print(" E) Exit")
  
  choice = input("input your choice: "+ "\n")
  if choice == "a" or choice == "A" :
    print("You chose addtion" +"\n")
    a = int(input("Enter first Number: "))
    b = int(input("Enter the second number: ")+ "\n")
    add(a,b)
  
  if choice == "b" or choice == "B" :
    print("You chose subtraction")
    a = int(input("Enter first Number: ")+ "\n")
    b = int(input("Enter the second number: ")+ "\n")
    sub(a,b)
  
  elif choice == "c" or choice == "C" :
    print("You chose multiplication"+ "\n")
    a = int(input("Enter first Number: "))
    b = int(input("Enter the second number: ")+ "\n")
    multiply(a,b)
  
  elif choice == "d" or choice == "D" :
    print("You chose division"+ "\n")
    a = int(input("Enter first Number: "))
    b = int(input("Enter the second number: ")+ "\n")
    div(a,b)
  elif choice == "e" or choice == "E" :
    print("Program ended")
    quit()
  
    
  

  

  
