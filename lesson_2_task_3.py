
a = int(input('enter num > 0: '))
backwards = ''

while a > 0:
    ld = a % 10
    backwards += str(ld)
    a //= 10
print(backwards)




