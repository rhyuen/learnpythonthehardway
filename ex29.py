people = 21
cats = 30
dogs = 15

if people < cats:
  print("There are more cats than people.")

if people > cats:
  print("there are more people than cats.")

if people < dogs:
    print("There are more dogs than people.")

if people > dogs:
    print("There are more people than dogs.")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

#study drill
if people > dogs:
    print("There are more people than dogs.")
    if people > cats:
        print("There are more people than cats.")
    print("There are more cats than people.")
