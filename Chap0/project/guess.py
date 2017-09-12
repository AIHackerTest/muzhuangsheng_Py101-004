import random

numbers = random.sample(range(10), 4)
while numbers[0] == 0:
    numbers = random.sample(range(10), 4)
answer = [str(n) for n in numbers]

print('Welcome and guess!')
print('The answer is a four-digit random number.')
print('All four digits are different and the first digit is not 0.')
print("Now let's begin!")

n = 10

while n > 0:
    g = input("you have %d guesses left: " % n)
    try:
        int(g)
        guess = [n for n in g]
        if guess[0] == '0':
            print('The first digit should not be 0.')
        elif len(set(guess)) < 4:
            print('All four digits should be different.')
        else:
            n = n - 1
            count_a = 0
            count_b = 0
            for i in range(4):
                if guess[i] == answer[i]:
                     count_a = count_a + 1
                elif guess[i] in answer:
                     count_b = count_b + 1
            if count_a == 4:
                print('Right')
                break
            else:
                print("%dA%dB" % (count_a, count_b))
    except ValueError:
        print("Please make sure you type in an integer.")
else:
    a = ''.join(answer)
    print('Game over. The answer is %s' % a)
