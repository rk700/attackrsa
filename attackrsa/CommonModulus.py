#!/usr/bin/env python

import gmpy
import Utils

class CommonModulus(object):
    '''
    Hastad Broadcast Attack
    '''
    def __init__(self, n, es, cs):
        '''
        n: common modulus 
        e: array of public exponent
        cs: array of cipher text
        '''
        self.n = n
        self.es = es
        self.cs = cs
    def decrypt(self):
        x,y = Utils.eGCD(self.es[0], self.es[1])
        if x < 0:
            x = -x
            self.cs[0] = Utils.modInv(self.cs[0], self.n)
        if y < 0:
            y = - y
            self.cs[1] = Utils.modInv(self.cs[1], self.n)
        p = (pow(self.cs[0], x, self.n)*pow(self.cs[1], y, self.n))%self.n
        return p
