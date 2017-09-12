from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print("You like this script?", end = ' ')
attitude = input()
print("So you said: %r" % attitude)

# python3 py13.py hello beautifual world
# yes
# The script is called: py13.py
# Your first variable is: hello
# Your second variable is: beautifual
# Your third variable is: world
# You like this script? yes
# So you said: 'yes'
