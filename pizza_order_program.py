import sys
import time
def printy(text, delay=0.05):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

printy("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

#Write your code below this line 👇
if size =="S":
    bill = 15
    if add_pepperoni=="Y":
        bill+=2
elif size =="M":
    bill = 20
    if add_pepperoni=="Y":
        bill+=3
elif size =="L":
    bill = 25
    if add_pepperoni=="Y":
        bill+=3

if extra_cheese=="Y":
    bill+=1
printy(f"Your final bill is: ${bill}.")
