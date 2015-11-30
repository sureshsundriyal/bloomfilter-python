import math

# Fixup for Python3
try:
    xrange
except:
    xrange = range

_64_1 = int('1'*64, 2)

def _hashlist(hash, num):
    # Takes a 128-bit hash and creates 'num' number of hashes.
    hash = int(hash, 16)
    l = hash >> 64
    r = hash & _64_1
    return list(
                map(
                    lambda x: (l << 64) | (x*r),
                    xrange(1, num+1)
                )
           )

class BloomFilter(object):
    def __init__(self, count=10000, error=0.01):
        self.count = count # Count(n)
        self.error = 0.01 # Error(p)
        self.nbits = (-1*count*math.log(error))/(math.log(2)**2)
        self.nbits = int(math.ceil(self.nbits))
        self.nbits += (self.nbits % 8) # Bits (m)
        self.functions =  int(math.ceil(
                                (self.nbits/count) * math.log(2)))# Functions(k)

        self.bitarray = bytearray([0] * int(self.nbits/8))
        self.items = 0

    def add(self, hash):
        hashlist = _hashlist(hash, self.functions)

        for hash in hashlist:
            x = hash % self.nbits
            self.bitarray[x//8] |= 1<<(x%8)

        self.items += 1

    def contains(self, hash):
        hashlist = _hashlist(hash, self.functions)

        for hash in hashlist:
            x = hash % self.nbits
            if not (self.bitarray[x//8] & 1<<(x%8)):
                return False

        return True

    def __contains__(self, hash):
        return self.contains(hash)
