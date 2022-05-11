import sys
import time
def printy(text, delay=0.05):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()
  
printy("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your partner name? \n")

combined=name1.lower()+name2.lower()
true=combined.count("t")+combined.count("r")+combined.count("u")+combined.count("e")
# print(true)
love=combined.count("l")+combined.count("o")+combined.count("v")+combined.count("e")
true_love=int(str(true)+str(love))
if true_love<10 or true_love>90:
    printy(f"Your score is {true_love}, Kono chance Nai 😒 ")

elif true_love>40 and true_love<60:
    printy(f"Your score is {true_love}, O MA GO TURU LOVE 😍 ")

else:
    printy(f"Your score is {true_love}, Effort dena padega 😪 ")

