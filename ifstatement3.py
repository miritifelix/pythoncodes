num1 = float(input("Enter the first no.: ")) #makes sure the input is a number since python converts to string
op = input("Enter the operator: ") #accepts the operato
num2 = float(input("Enter the second no.: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("invalid op")
