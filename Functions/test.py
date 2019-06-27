import random 

print('This is a number guessing game. Guess a number between 1 and 20.')
print('You have 6 chances')
secret = random.randint(1,20)
for i in range(1,7):
    print ('>> ')
    guess = int(input())
    if guess > secret:
        print('Guess too high. Try guessing a smaller number')
    elif guess < secret: 
        print('Guess too low. Try guessing a larger number')
    else:
        break  # for when the guess is correct.
if guess == secret:
    print('Good Job. You guessed the number in '+ str(i)+' tries.')
else:
    print('You ran out of chances.')
