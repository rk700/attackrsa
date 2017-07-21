#!/usr/bin/env python
import gmpy

def eGCD(a, b):
    '''
    Extended Euclidean gcd. Return g,x,y such that ax+by=g=gcd(a,b)
    '''
    u, u1 = 1, 0
    v, v1 = 0, 1
    g, g1 = a, b
    while g1:
            q = g // g1
            u, u1 = u1, u - q * u1
            v, v1 = v1, v - q * v1
            g, g1 = g1, g - q * g1
    return u, v

def modInv(a, m):
    '''
    Return r such that a*r mod m = 1
    '''
    return gmpy.invert(a, m)

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



