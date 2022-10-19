print(str("Hi"))




timer = 0
baked_good = []
bakery = 0

while bakery == 0 :
  answer = input ("What kind of baked good do you want to make?")
  if (answer == "cookies" or answer == "cake" or answer == "pie"):
    baked_good.append(answer)
    if (answer == "cookies"):
      timer = 12
    if (answer == "cake"):
      timer = 30
    if (answer == "pie"):
      timer = 20
    timer = timer + 1
    while timer > 0:
      timer = timer - 1
      print("You have " + str(timer) + " minutes left")
      if timer == 0:
        print(answer + " is out of the oven!")
  if (answer != "cookies" and  answer != "cake" and answer != "pie"):
    print("I don't recognize that!")
