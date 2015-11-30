bloomfilter-python
==================

A simplistic pure python bloomfilter implementation.

The bloomfilter expects the users to hash the object that is being tracked and
the resulting 128-bit hexdigest is expected to be passed in to the
`Bloomfilter.add()` method.

Example:
--------

```
>>> import bloomfilter
>>> from hashlib import md5
>>> dig = md5()
>>> dig.update(b'hello world')
>>> bf = bloomfilter.BloomFilter()
>>> bf.add(dig.hexdigest())
>>> dig.hexdigest() in bf
True
```
