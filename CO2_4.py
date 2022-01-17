"Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square."
import math

def digit_check(number):
    while(number>0):
        num=number%10
        number=number//10
        if num%2!=0:
            return 0
    return 1
  
lowelimit=int(input("enter lower_limit"))   
uperlimit=int(input("enter upper_limit"))   
 
lst=[]
for number in range(lowelimit,uperlimit):
    if digit_check(number):  
        
        sqrt=int(math.sqrt(number)) 

        if sqrt*sqrt==number:
            lst.append(number)
print(lst)
