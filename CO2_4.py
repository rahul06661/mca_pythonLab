"Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square."
import math

def digit_check(number):
    while(number>0):
        num=number%10
        number=number//10
        if num%2!=0:
            return 0
    return 1
        
lst=[]
for number in range(1000,9999):
    if digit_check(number):  
        
        sqrt=int(math.sqrt(number)) 
        print(sqrt)

        if sqrt*sqrt==number:
            lst.append(number)
    