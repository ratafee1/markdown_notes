from random import sample, shuffle

digits = 3
guesses = 10
print('I am thinking of a', digits, 'digit number.')
print('Try to guess what it is.')
print('Here are some clues:')
print('When I say:    That means:')
print('  pico         One digit is correct but in the wrong position.')
print('  fermi        One digit is correct and in the right position.')
print('  bagels       No digit is correct.')
print('There are no repeated digits in the number.')

# Create a random number
letters = sample('0123456789', digits)
if letters[0] == '0':
    letters.reverse()

number = ''.join(letters)
print(number)

print('I have thought up a number.')
print('You have ', guesses, 'guesses to get it')

counter = 1

while True:
    print('Guess #', counter)
    guess = input()
    print(isinstance(guess, str))

    if len(guess) != digits:
        print('Wrong number of digits. Try again!')
        continue

    # Create the clues.
    clues = []
    for index in range(digits):
        if guess[index] == number[index]:
            clues.append('fermi')
        elif guess[index] in number:
            clues.append('pico')

    shuffle(clues)

    if len(clues) == 0:
        print('bagles')
    else: print(''.join(clues))

    counter +=1

    if guess == number:
        print('you got it')
        break

    if counter > guesses:
        print('You ran out of guesses. The answer was', number)
        break
