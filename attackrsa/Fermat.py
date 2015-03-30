#!/usr/bin/env python

import gmpy
import RSABase

class Fermat(RSABase.RSABase):
    def __init__(self, n, limit=10000):
        super(Fermat, self).__init__(n)
        self.limit = limit
    def crack(self):
        a = gmpy.sqrt(self.n)
        max = a + self.limit
        while a < max:
            b2 = a*a - self.n
            if b2 >= 0:
                b = gmpy.sqrt(b2)
                if b*b == b2:
                    break
            a += 1
        if a < max:
            self.p = a+b
            self.q = a-b
            return True
        else:
            return False

        


