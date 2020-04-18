import string

letters = list(string.ascii_lowercase)
a = input("Name the letter to get it's index in english abs: ")
try:
    print(letters.index(a) + 1)
except:
    print("the code isn't correct, check if it's a letter")
