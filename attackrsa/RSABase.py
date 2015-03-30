#!/usr/bin/env python

import Utils

class RSABase(object):
    def __init__(self, n, e=3, d=None, p=None, q=None):
        self.n = n
        self.e = e
        self.d = d
        self.p = p
        self.q = q
    def getPrivKey(self):
        '''
        Compute private key d if the factorization n=pq is known
        '''
        if self.d:
            return self.d
        elif self.p and self.q and self.e:
            phi = (self.p-1) * (self.q-1)
            self.d = Utils.modInv(self.e, phi)
            return self.d
        else:
            print "Cannot compute private key without factorization"
    def decrypt(self, ct):
        if self.d:
            return pow(ct, self.d, self.n)
        else:
            print "Cannot decrypt without private key"
