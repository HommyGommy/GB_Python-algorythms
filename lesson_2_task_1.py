
while True:
    op = input("choose the first operation: '+' or '-' or '*' or '/', to finish press 0: ")
    if op == "0":
        break
    a = float(input("enter first num: "))
    b = float(input("enter second num: "))
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == ".":
        print(a / b)
    elif op == "/" and b == 0:
        print("zero div error")
    else:
        print("check input")
        break

