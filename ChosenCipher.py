#!/usr/bin/env python

import Utils

class ChosenCipher(object):
    def __init__(self, n, e, c):
        self.n = n
        self.e = e
        self.c = c
    def mulFactor(self, f):
        return (self.c * pow(f, self.e, self.n))%(self.n)
    def decrypt(self, f, newP):
        inv = Utils.modInv(f, self.n)
        return (newP*inv)%(self.n)
        
