import random


r = random.randrange(1,11)  #start 1 to end 10

while True:
  u = int(input("Input a number 1 to 10: "))
  if u == r :
    print (f"You Win!! Number is {r}")
    break
  else:
    print (f"Nice Try, You loss!!")
    print (f"Your number {u}; \nComputer number {r}")