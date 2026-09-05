import os
import random

os.system("clear")
number = random.randint(1, 9)
initial = input("Please input the first, middle, and last initial of the POI (e.g. pcp): ")
os.system("clear")
state = input("Please input the state of the POI (e.g. KS): ")
file = os.getcwd() + "/casenumber.txt"
if os.path.isfile(file):
  with open(file, "r") as f:
    current_number = f.read()
    new_number = int(current_number)
    new_number += 1
    os.system("clear")
    print("Your case number is: " + initial + "-" + state + "-" + str(new_number))
    f.close()
    with open(file, "w") as f:
      f.write("" + str(new_number))
else:
  with open(file, "w") as f:
    number = f.write("1")
    os.system("clear")
    print("Your case number is: " + initial + "-" + state + "-1")