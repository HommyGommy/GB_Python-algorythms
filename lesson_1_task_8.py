print("let's compare your three numbers")
a = int(input("enter the first num >0: "))
b = int(input("enter the second num >0: "))
c = int(input("enter the third num >0: "))

if b < a < c or c < a < b:
    print(f"avg is {a}")
elif a < b < c or c < b < a:
    print(f"avg is {b}")
else:
    print(f"avg is {c}")