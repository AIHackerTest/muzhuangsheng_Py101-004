import random

answer = random.randint(1, 20)

n = 10

while n > 0:
    g = input("Guess the the number, you have %d guesses left: " % n)
    try:
        guess = int(g)
        n = n - 1
        if guess == answer:
            print('Right!')
            break
        elif guess > answer:
            print('too large, try again.')
        else:
            print('too small, try again')
    except ValueError:
        print("Please make sure you type in an integer")
else:
    print('Game over.')
