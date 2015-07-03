def cheese_and_crackers(cheese, crackers):
  print("%d cheese." %(cheese))
  print("%d crackers." %(crackers))
  print("Get a blanket for a party!\n")

print("Args directly to method")
cheese_and_crackers(20, 30)

print("Variables passed as args.")
amt_cheese = 10
amt_crackers = 50
cheese_and_crackers(amt_cheese, amt_crackers)

print("Computation in args of method")
cheese_and_crackers(10+20, 20+30)

print("Combination of Computation and Variables as Args")
cheese_and_crackers(amt_cheese + 3, amt_crackers + 4)

def add(first, second):
    print(first + second)

add(1,2)
add(2,3)
add(3,4)
