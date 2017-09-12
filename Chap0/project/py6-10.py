# ex6
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x) # There are 10 types of people.
print(y) # Those who know binary and those who don't.

print("I said: %r." % x) # I said: 'There are 10 types of people'.
print("I also said: '%s'." % y) # I also said: 'Those who know binary and those who don't.'

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious) # Isn't that joke so funny?! False

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e) # This is the left side of ...a string with a right side.


# ex7
print("Mary had a little lamb.") # Mary had a little lamb.
print("Its fleece was white as %s." % 'snow') # Its fleece was white as snow.
print("And everywhere that Mary went.") # And everywhere that Mary went.
print("." * 10) # what'd that do? ..........

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what hapens
# in Python2
# print end1 + end2 + end3 + end4 +end5 +end6,
# print end7 + end8 + end9 + end10 + end11 + end12
print(end1 + end2 + end3 + end4 +end5 +end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12) # Cheese Burger

print(end1 + end2 + end3 + end4 +end5 +end6) # Cheese
print(end7 + end8 + end9 + end10 + end11 + end12) # Burger
# whether there is a comma or not, 2 strings show in 2 lines


# ex8
formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4)) # 1 2 3 4
print(formatter % ("one", "two", "three", "four")) # 'one' 'two' 'three' 'four'
print(formatter % (True, False, False, True)) # True False False True
print(formatter % (formatter, formatter, formatter, formatter)) # '%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
print(formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)) # 'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'


# ex9
# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fir Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days) # Here are the days: Mon Tue Wed Thu Fir Sat Sun
print("Here are the months: ", months) # Here are the months: Jan
# Feb
# Mar
# Apr
# May
# Jun
# Jul
# Aug

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""") # There's something going on here.
# With the three double-quotes.
# We'll be able to type as much as we like.
# Even 4 lines if we want, or 5, or 6.


# ex10
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat) #       I'm tabbed in.
print(persian_cat) # I'm split
# on a line.
print(backslash_cat) # I'm \ a \ cat.
print(fat_cat) # I'll do a list:
#      * Cat food
#      * Fishies
#      * Catnip
#      * Grass

print("I am 6'2\" tall.") # escape double-quote inside string. I am 6'2" tall.
print('I am 6\'2" tall.') # excape single-quote inside string. I am 6'2" tall.

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print("%s\r" % i, end = '')
