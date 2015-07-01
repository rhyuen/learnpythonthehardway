print ("How old are you?")
age = input()

print ("How tall are you?")
height = input()

print ("How much do you weight?")
weight = input()

print ("So, you're %r old, %r tall and %r heavy" %(age, height, weight))


print ("How many cars do you have?")
car = int(input())
print("How many houses do you have?")
house = int(input())
print("How many boats do you have?")
boat = int(input())
print ("So you have %r car(s), %r house(s) and %r boats. You have %r assets." %(car, house, boat, car + house + boat))
