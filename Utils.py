#!/usr/bin/env python


def eGCD(a, b):
    '''
    Extended Euclidean gcd. Return g,x,y such that ax+by=g=gcd(a,b)
    '''
    if a == 0: 
        return (b, 0, 1)
    else:
        g, y, x = eGCD(b%a, a)
        return (g, x-(b//a)*y, y)

def modInv(a, m):
    '''
    Return r such that a*r mod m = 1
    '''
    g, x, y = eGCD(a, m)
    if g != 1:
        print("no inverse")
        return None
    else:
        return x % m

def CRT(ds, rs):
    '''
    Chinese Remainder Theorem
    ds: array of dividers
    rs: array of remainders
    Return the number s such that s mod ds[i] = rs[i]
    '''
    length = len(ds)
    if not length == len(rs):
        print "The lengths of the two must be the same"
        return None

    p = i = prod = 1 
    s = 0
    for i in range(length): 
        prod *= ds[i]
    for i in range(length):
        p = prod // ds[i]
        s += rs[i] * modInv(p, ds[i]) * p
    return s % prod



