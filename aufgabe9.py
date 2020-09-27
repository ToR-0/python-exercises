#Write a Python program to test whether a number is within 100 of 1000 or 2000. 
def near_thouthand(n):
         return ((abs(1000 - n) <=100) or  (abs(2000 - n) <= 100))
print (near_thouthand(1000))
print (near_thouthand(900))
print (near_thouthand(800))
print (near_thouthand(2200))
