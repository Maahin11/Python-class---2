# -*- coding: utf-8 -*-
"""213902127-Mahin-21-10-2024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Zz9mgW7c8VfvEbVhXJx4By0QYzp0ukdN
"""

print(123)
print("Hello Worl!d")

x = 10
y = 12.2
print(x)
print(y)
print(x,y)
print('x: ',x,'y: ',y)
print('x: ',str(x),'y: ',str(y))

x = x+10
print(x)

PI = 3.14
radius = 5
area = PI * radius **2
print("The area is: ",area)

a = 10
b = 20
a,b=b,a
print(a,b)

P = 75
R = 25
T = 5
SI = (P*R*T)/100
print(SI)

celcius = 25
fahrenheit = (celcius*9/5)+32
print(fahrenheit)

length = 10
width = 20
area = length * width
rectangle = length * 2 + width * 2
print(area)
print(rectangle)

print (type(12.5))
print (type("Mahin"))
print (type(12))

print(float(99)+100)

noun = 'Mahin'
day  ='Monday'
str_ = f'''How are you Mr.{noun}.You are invited to my house on {day}.{noun} don't miss the opportunity'''
print(str_)

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

pay = hours * rate
print(f"Pay:{pay}")

result = print(5, "is a number")
print("Return value of print():", result)

a1 = "All"
b2 = "work"
c3 = "and"
d4 = "no"
e5 = "play"
f6 = "makes"
g7 = "Jack"
h8 = "a"
i9 = "dull"
j10 = "boy"

print(a1, b2, c3, d4, e5, f6, g7, h8, i9, j10)

result = 6 * (1 - 2)

print(result)

# Assign a value to bruce
bruce = 6

# Now bruce + 4 will evaluate to 10
result = bruce + 4

# Output the result
print(result)

# madlib.py

# Ask the user for different types of words
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")
plural_noun = input("Enter a plural noun: ")
past_verb = input("Enter a past tense verb: ")

# Generate a silly madlib-style paragraph using the inputs
print("\nHere is your ridiculous story:\n")
print(f"Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb}.")
print(f"Every day, they would gather all the {plural_noun} and {verb} until the sun set.")
print(f"But one day, the {noun} {past_verb} too much, and they ended up in a tree!")
print(f"Now, whenever someone mentions {plural_noun}, the {adjective} {noun} smiles {adverb}.")

# End of madlib.py

noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
plural_noun = input("Enter a plural noun: ")
verb_past = input("Enter a verb in past tense: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")

story = f"""
Once upon a time, there was a {adjective} {noun1} who loved to {verb} {adverb}. One day, it found a group of {plural_noun} playing with a {noun2}.
The {noun1} {verb_past} with joy and decided to join them.
Together, they all {verb}ed happily ever after!
"""

print(story)