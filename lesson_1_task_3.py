import random
import string

# task a)
print("For random int please")
int_start = input("select the low boarder for your rand int: ")
int_stop = input("and the high boarder for your rand int: ")
try:
    rand_int = random.randint(int(int_start), int(int_stop))
    print(rand_int)
except:
    print("code isn't correct, make sure you're inputting an int and stop > start ")

# task b)
print("For random float please")
float_start = input("select the low boarder: ")
float_stop = input("and the high boarder: ")
try:
    rand_float = random.uniform(float(float_start), float(float_stop))
    print(rand_float)
except ValueError:
    print("code isn't correct, make sure you're inputting a float and stop > start ")

# task c)
print("For random symbol please")
a = input("select the start: ")
b = input("and stop: ")

rand_sym_index = random.randint(int(ord(a)), int(ord(b)+1))
answer = chr(rand_sym_index)

print(answer)
