import sys
import time
def printy(text, delay=0.05):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    
name = input("Enter your name :)")
printy( "I love you ❤  " + name )
printy( f"I love you ❤  {name}")



# a = float(input("Enter first number : "))
# b = float(input("Enter second number : "))

# print ("Which operaton do you want ? ")

# print ("1. + \n2. - \n3. * \n4. /")
# op = input("Choose any number :")
# if(op=='1'):
#     print(a+b)
# elif(op=='2'):
#     print(a-b)
# elif(op==3):
#     print(a*b)

