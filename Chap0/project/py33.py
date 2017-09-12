i = 0
numbers = []

while i < 6:
    print("At the top i is %d" % i) # At the top i is 0, ...
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers) # Numbers now: [0], ...
    print("At the bottom i is %d" % i) # At the bottom i is 1, ...


print("The numbers: ") # The numbers:

for num in numbers:
    print(num) # 0\n1\n2\n3\n4\n5
