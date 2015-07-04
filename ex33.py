i = 0
numbers = []

while i < 6:
  print("At the top i is %d" % i)
  numbers.append(i)

  i += 1
  print("Numbers now: ", numbers)
  print("At the bottom i is %d" % i)

print("The numbers: ")
for number in numbers:
  print(number)


def loop(list, limit):
    i = 0
    while i < limit:
        list.append(i)
        print(list)
        i+= 1

loop([], 20)

def loop_step(list, limit, step):
    i=0
    while i < limit:
        list.append(i)
        print(list)
        i+=step

loop_step([1], 10, 3)
