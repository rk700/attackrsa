#!/usr/bin/env python

import gmpy
import Utils

class Hastad(object):
    '''
    Hastad Broadcast Attack
    '''
    def __init__(self, ns, e, cs):
        '''
        ns: array of n
        e: public exponent
        cs: array of cipher text
        '''
        self.ns = ns
        self.e = e
        self.cs = cs
    def decrypt(self):
        s = Utils.CRT(self.ns, self.cs)
        pt, perfect = gmpy.root(s, self.e)
        if perfect:
            return pt
        else:
            print "Cannot find %dth root of %s" % (self.e, hex(s))


        
