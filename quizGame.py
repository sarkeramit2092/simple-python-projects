print("Welcome to my comuter quiz!")
print("*" * 20)

playing = input("Do you want to play? ")

if playing != "yes":
  quit()

print("Okay! Let' Play : ")
print("*" * 20)

result = 0
q = 0

while True:
  answer = input("What does CPU stand for? ")
  q +=1
  if answer.lower() == "central processing unit":
    print("Correct!")
    result += 1
  else:
    print("Incorrect!")

  answer = input("What does GPU stand for? ")
  q +=1
  if answer.lower() == "graphics processing unit":
    print("Correct!")
    result += 1
  else:
    print("Incorrect!")

  answer = input("What does RAM stand for? ")
  q +=1
  if answer.lower() == "random access memory":
    print("Correct!")
    result += 1
  else:
    print("Incorrect!")

  answer = input("What does PSU stand for? ")
  q +=1
  if answer.lower() == "power supply unit":
    print("Correct!")
    result += 1
    break
  else:
    print("Incorrect!")

print(f"Your Score is {result} out of {q} questions!!")
