
import math
def paint_calc(height,width,cover):
    number_of_cans=math.ceil((height*width)/cover) 
    #round funtion gives 2.3 = 2 so I have used math.ceil gives nxt number 3 
    print(f"You'll need {number_of_cans} cans of paint.")

h = int(input("Height of wall: "))
w = int(input("Width of wall: "))
coverage = 5 #Let, one paint can covers 5 sq.mtr
paint_calc(height=h, width=w, cover=coverage)

