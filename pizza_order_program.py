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
if size.upper() =="S":
    bill = 150
    if add_pepperoni.upper()=="Y":
        bill+=20
elif size.upper() =="M":
    bill = 200
    if add_pepperoni.upper()=="Y":
        bill+=30
elif size.upper() =="L":
    bill = 250
    if add_pepperoni.upper()=="Y":
        bill+=30

if extra_cheese.upper()=="Y":
    bill+=10
printy(f"Your final bill is: ₹ {bill}.")
