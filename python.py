# Importing the necessary modules
# importing the random module
import random #This will perform random generations
a=random.randint(1,20)
print("The properties followed by random number in a given range (1,) are: ")
if a>0:
 print(f"{a} is a positive number")
else:
 print(f"{a} is a negative number")
if a%2==0:
 print(f"{a} is an even number")
else:
 print(f"{a} is a odd number")
x = 0
if a>1:
    for i in range(2,a-1):
        if a%i==0:
            x+=1
if x>1:
 print(f"{a} is a composite number")
else:
 print(f"{a} is a prime number")
