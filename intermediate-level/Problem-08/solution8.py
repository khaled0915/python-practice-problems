def calculator():
    command = input("Enter command: ").split()
    
    if len(command) != 3:
        print("Invalid input. Example: add 5 7")
        return

    operation, num1, num2 = command
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Please enter valid numbers.")
        return

    if operation == "add":
        print(num1 + num2)
  
   
    else:
        print("Unknown command. Use add, subtract, multiply, divide.")

calculator()
