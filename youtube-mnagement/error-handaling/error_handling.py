file = open("youtube.txt", "w")

try:
  file.write("python at weekend")

finally:
  file.close()

#---------------------------------

with open("youtube.txt", "w") as file:
  file.write("python developer amit 2025")