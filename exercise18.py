import string
import random

computer = random.choices(string.digits, k=4)
print(computer)

guesses = 0
while True:
    person = (input('Guess a 4 digit number: '))
    if person == ''.join(computer):
        print('you guessed right!')
        break
    if person == 'exit':
        break

    if int(person) < 1000:
        person = (input('Guess a 4 digit number: '))

    else:
        cow = 0
        bull = 0
        guesses += 1

        if computer[0] == person[0]:
            cow += 1
        if computer[1] == person[1]:
            cow += 1
        if computer[2] == person[2]:
            cow += 1
        if computer[3] == person[3]:
            cow += 1
        print(cow)

        cb = len([num for num in computer if num in person])
        bull = cb - cow
        print(bull)

    print('cow: {} and bull: {}. guesses {}'.format(cow,bull,guesses))
