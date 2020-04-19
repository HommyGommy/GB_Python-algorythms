import random

quiz = random.randint(0, 101)
attempts = 10

while attempts > 0:
    guess = int(input(f"try to guess the number between 0 and 100, you've got {attempts} attempts: "))
    if guess == quiz:
        print(f'hooray! the number is {guess}')
        break
    elif guess > quiz:
        attempts -= 1
        print(f'go lower')
    elif guess < quiz:
        attempts -= 1
        print(f'go higher')
else:
    print('such a looser, better try next time')