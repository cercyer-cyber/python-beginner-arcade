again= "yes"

while again.strip().lower() == "yes":
    while True:
        try:
            num1 = float(input("first number:"))
            break
        except ValueError:
            print("That's not a number, try again")
    while True:
        try:
            num2 = float(input("second number:"))
            break
        except ValueError:
            print("That's not a number, try again")
    while True:
        op = input("operator (+,-,*,%,**,/):")
        if op in ["+", "-", "*", "%", "**", "/"]:
            break
        else:
            print("Invalid operator, try again")
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "%":
        print(num1 % num2)
    elif op == "**":
        print(num1 ** num2)
    elif op == "/":
        if num2 == 0:
            print("division by zero is not allowed")
        else:
            print(num1 / num2)
    while True:
        again = input("do another? (yes/no):")
        if again.strip().lower() in ["yes", "no"]:
            break
        else:
            print("Invalid input, please enter 'yes' or 'no'")

    if again.strip().lower() != "yes":
        print("Sayonara!👋")