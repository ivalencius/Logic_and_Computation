# Ilan Valencius
import random
import sys
sys.setrecursionlimit(2500)

def fermatTest(n,ntrials):
    if (ntrials == 0):
        return True
    a = random.randrange(1,n-1)
    if (pow(a,n-1,n) != 1): 
        return False
    else:
        return fermatTest(n,ntrials-1)

def fermatPrime(max, ntrials):
    rand_num = random.randint(0, max)
    while(not fermatTest(rand_num,ntrials)):
        rand_num = random.randrange(max)
    return rand_num

def main():
    max = random.randint(0,10**500)
    # set ntrials = 10 for P(false positive) < 0.1%
    ntrials = 10
    print("%d\n\n is a probably prime number between 0 and \n\n%d"%(fermatPrime(max,ntrials),max))
    
main()