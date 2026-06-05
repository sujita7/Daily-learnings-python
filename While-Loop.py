# It executes statements while the consitions is TRUE. As soon as the consition become FALSE, the interpreter come out of the while loop.
i = 0 
while(i<3):
  print(i)
  i = i+1
# o/p -> 0 1 2

# usually we use while loop for complex problems


# Do While Loop : It is not in python but what is Do While Loop -> Do While Loop basically means that the loop body will executes at once and then check while if it is true it execute again.

# in python if i want to emulate do while loop :
# -> we need to modify the while loop a bit in order to get similar behaviour to a do while loop .
# -> use a infinite while loop with a BREAK statement wrapped in an IF Statement that checks a given condition and BREAKS the iterration if that condition becomes True.

while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
        break
""" output->
Enter a positive number: 10
10
Enter a positive number: 3
3
Enter a positive number: 4
4
Enter a positive number: 5
5
Enter a positive number: 6
6
Enter a positive number: 0
0
"""


# BREAK Statement: Skips over a part of the code, Terminate the very loop it lies within, It Skips the loop, Breaking out of loop

# CONTINUE Statement: It skips the iteation not loop .


