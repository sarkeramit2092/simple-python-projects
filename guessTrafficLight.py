import random

l =["red","green","yellow"]

choice = random.choice(l)

while True:
  guess = input("Guess the traffic light: ")

  if guess.lower() == choice:
    print (f"You Win!! Traffic Light is {choice}")
    break
  else:
    print (f"Nice Try, You loss!!")
    print (f"You choice {guess} light; \nComputer choice {choice} light!!")
    