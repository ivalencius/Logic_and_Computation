# Ilan Valencius
import random

def fermatTest(n,ntrials):
    if (ntrials == 0):
        return True
    a = random.randint(2,n)
    if (pow(a,n-1,n) != 1): 
        return False
    else:
        return fermatTest(n,ntrials-1)
    
def main():
    random_num1 = random.getrandbits(6700)
    random_num2 = random.getrandbits(6700)