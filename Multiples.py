what = input("Do you want decimal or normal multiples?")
if what == "normal":
  var = int(input("What multiples do you want?"))
  ran = int(input("Up to what number?"))
  multiples_of_four = [i * var for i in range(ran)]
  print(multiples_of_four)
if what == "decimal":
  var = float(input("What multiples do you want?"))
  ran = int(input("Up to what number?"))
  multiples_of_four = [i * var for i in range(ran)]
