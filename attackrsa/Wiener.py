#!/usr/bin/env python

from fractions import Fraction
import gmpy
import RSABase

def f2cf(nu, de):
    '''
    Fraction nu/de to continued fraction
    '''
    cf = []
    while de:
        qu = nu // de
        cf.append(qu)
        nu, de = de, nu - de*qu
    return cf

def cf2f(cf):
    '''
    Continued fraction to fraction
    '''
    f = Fraction(0, 1)
    for x in reversed(cf):
        try:
            f = 1 / (f+x)
        except ZeroDivisionError:
            return Fraction(0, 1)
    return 1/f

def cf2cvg(cf):
    '''
    Continued faction to convergents
    '''
    for i in range(1,len(cf)+1):
        yield cf2f(cf[:i])

class Wiener(RSABase.RSABase):
    def __init__(self, n, e):
        super(Wiener, self).__init__(n, e)
    def crack(self):
        for cvg in cf2cvg(f2cf(self.e, self.n)):
            k = cvg.numerator
            if k == 0:
                continue
            d = cvg.denominator
            phi = (self.e*d-1)//k
            nb = self.n - phi + 1
            squ = nb*nb-4*self.n
            if squ < 0:
                continue
            root = gmpy.sqrt(squ)
            if root*root == squ and not (nb+root)&1:
                self.p = (nb+root)>>1
                self.q = (nb-root)>>1
                self.d = d
                return True
        return False
                
                
