import string

print("Select two letters")
abc = list(string.ascii_lowercase)
a = input("first letter: ")
b = input("second letter: ")

try:
    print(f"first letter's index is {abc.index(a)+1}")
    print(f"first letter's index is {abc.index(b)+1}")
    print(f"there are {(abc.index(b)+1) - (abc.index(a)+1) -1} letters between")
except:
    print("check the code")