__author__ = "Suresh Sundriyal"
__version__ = "0.0.1"
__license__ = "BSD 2-clause"

import math

# Fixup for Python3
try:
    xrange
except:
    xrange = range

_64_1 = int('1'*64, 2)

def _hashlist(hash, hash_count):
    # Takes a 128-bit hash and creates 'num' number of hashes.
    hash = int(hash, 16)
    l = hash >> 64
    r = hash & _64_1
    return list(
                map(
                    lambda x: (l << 64) | (x*r),
                    xrange(1, hash_count+1)
                )
           )

class BloomFilter(object):
    def __init__(self, capacity=10000, error_rate=0.01):
        self.capacity = capacity # Count(n)
        self.error_rate = error_rate # Error(p)
        self.nbits = (-1*capacity*math.log(error_rate))/(math.log(2)**2)
        self.nbits = int(math.ceil(self.nbits))
        self.nbits = ((self.nbits // 8) + 1) * 8 # Bits (m)
        self.hash_count =  int(math.ceil( # Number of hashes(k)
                                (self.nbits/capacity) * math.log(2)))

        self.bitarray = bytearray([0] * int(self.nbits/8))
        self.items = 0

    def add(self, hash):
        hashlist = _hashlist(hash, self.hash_count)

        x = 0
        for hash in hashlist:
            x = hash % self.nbits
            self.bitarray[x//8] |= 1<<(x%8)

        self.items += 1

    def contains(self, hash):
        hashlist = _hashlist(hash, self.hash_count)

        for hash in hashlist:
            x = hash % self.nbits
            if not (self.bitarray[x//8] & 1<<(x%8)):
                return False

        return True

    def __contains__(self, hash):
        return self.contains(hash)
