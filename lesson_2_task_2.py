even = ''
odds = ''

nat = input('Please enter any num > 0: ')

for i in str(nat):
    if int(i) % 2 == 0:
        even += i
    else:
        odds += i

print(f'there are {len(even)} even digits and {len(odds)} odds')