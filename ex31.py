print("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = input("> ")

if door == "1":
  print("There's a giant bear here eating a cheesecake.  What do you do?")
  print("1. Take the cake.")
  print("2. Scream.")

  bear = input("> ")
  if bear == "1":
    print("The bear eats your face off.")
  elif bear == "2":
      print("The bear eats your legs off.")
  else:
    print("Well, doing %s is probably better.  Bear runs away." %(bear))

elif door == "2":
    print("You stare into the endless abyss of Cthulhu's eyes.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")
    if insanity == "1" or insanity == "2":
        print("Your body survives but your mind does not.")
    else:
        print("You go insane and your eyes fry.")

else:
    print("You stumble and accidentally kill yourself.")
