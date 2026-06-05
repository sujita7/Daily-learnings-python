# Loops are basically resuable chunks of codes,
# It is used to perform a action repeatedly,
# For Loop: it can iterate over a sequence of iterable objects in python. over a string, lists, tuples,sets, and dictionaries.



colors = ["RED", "YELLOW", "GREEN"]
for i in colors:
  print(i) 
# output ->
#Red
#Yellow
#Green
  for j in i:
    print(j, end=", ")
    # o/p -> RED R,E,D  YELLOW Y,E,L,L,O,W like that 


# Range -> it have (start, stop, step)
for k in range(0,9,3):
    print(k)
  # o/p -> 0 3 6
