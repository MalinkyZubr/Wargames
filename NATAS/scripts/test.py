ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = list(filter(myFunc, ages))

for x in adults:
  print(x)