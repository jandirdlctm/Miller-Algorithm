import random
import math

def StandardTest(x):
    state = 1
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            state=0
            return False
            break
        else:
            continue
    if state == 1:
        return True
    return False

def MillerPrime(n):
    for i in range(10):
        ok = MillersTest(n)
        if ok == False:
            return False  
        
    return True 

def MillersTest(n):
    if n == 2:
        return True
    b = random.randint(2, n-1)
    #find s and t such that 2^s*t == n-1
    s = 0
    t = n-1
    while t % 2 == 0:
        s += 1
        t = int(t // 2)

    #if 2^t% n is  1 then return True
    if pow(b,t,n) == 1: # power modulus function is much more efficient
        return True

    for j in range(s):
        if pow(b,pow(2,j) * t,n) == n - 1:
            return True

    return False




def main():
    print(MillersTest(101)) #should print true
    print(MillersTest(105)) #should print false

    #test for small numberes
    for i in range(2, 1000000):
        if MillerPrime(i) != StandardTest(i):
            print("Error inconsistent for integer", i)

    #test for big numbers
    x = 55249670751805114655765974429986162664726206020744723778493631382633884817280127867822310417337383310631433769431407398925167751695352120507489885110559435005960351366573293881307493461711711792403571
    print(MillerPrime(x))
    #test for a big composite number -> multiplying 2 big prime numbers
    y = 55249670751805114655765974429986162664726206020744723778493631382633884817280127867822310417337383310631433769431407398925167751695352120507489885110559435005960351366573293881307493461711711792403571 * 55249670751805114655765974429986162664726206020744723778493631382633884817280127867822310417337383310631433769431407398925167751695352120507489885110559435005960351366573293881307493461711711792403571
    print(MillerPrime(y))
main()








