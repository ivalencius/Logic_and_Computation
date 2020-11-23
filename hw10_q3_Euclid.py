# Ilan Valencius
import random
import sys
sys.setrecursionlimit(9000)

def extended_Euclid(n1,n2):
    if n2==0:
        return (1,0,n1)
    else:
        (q,r) = divmod(n1,n2)
        (a,b,d) = extended_Euclid(n2,r) 
    return (b, a-b*q, d)   

def main():
    random_num1 = random.getrandbits(6700)
    random_num2 = random.getrandbits(6700)
    (a, b, gcd) = extended_Euclid(random_num1, random_num2)
    print("Number 1 = \n%d" %(random_num1))
    print("Number 2 = \n%d"%(random_num2))
    print("a=\n%d\nb=\n%d\ngcd=%d"%(a,b,gcd))
    
main()