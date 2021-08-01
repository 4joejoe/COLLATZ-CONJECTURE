# COLLATZ CONJECTURE
import random 
# a = random.randint(2,10)
a=20
print(f'Generated Random Number:{a}')
# Helper Function
def oddAlgo(num):
    return num*3+1
def evenAlgo(num):
    return num/2
# main algo
    

def algo(num):
    if num%2!=0 and num!=1:
        nextInput = oddAlgo(num)
        print(nextInput)
        ll = input('>')
        algo(nextInput)
    elif num%2==0:
        nextInput = evenAlgo(num)
        print(nextInput)
        ll = input('>')
        algo(nextInput)
    elif num==1:
        quit()

while a!=1:
    algo(a)