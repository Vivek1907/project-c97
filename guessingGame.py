import random

print('Number Guessing Game')
print('Guess a number (1 - 9)')

random_number = random.randrange(1, 9)
count = 5

while count > 0 :
    number = int(input('Enter your guess:- '))
    if number == random_number:
        print('Congratulations you Won!!!')
        break
    elif number < random_number:
        print('Your guess is too low! Try a number greater than ' + str(number))
    elif number > random_number:
        print('Your guess is too high! Try a number lesser than ' + str(number))
    count -= 1

if count == 0 :
    print("You Lose!")
