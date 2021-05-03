import math
import mmh3
from bitarray import bitarray
import random
import string

class BloomFilterNonPartitioned(object):

    '''
    Class for Bloom filter, using murmur3 hash function
    '''

    def __init__(self, hash_count, size, fp_prob):

        # False positive probability in decimal
        self.fp_prob = fp_prob

        # Size of bit array to use
        self.size = size
        # self.size = self.get_size(items_count, fp_prob)

        # number of hash functions to use
        self.hash_count = hash_count

        # Bit array of given size
        self.bit_array = bitarray(self.size)

        # initialize all bits as 0
        self.bit_array.setall(0)

    def add(self, item):

        digests = []
        for i in range(self.hash_count):

            digest = mmh3.hash(item, i) % self.size
            digests.append(digest)
            self.bit_array[digest] = True


    def check(self, item):

        for i in range(self.hash_count):
            
            digest = mmh3.hash(item, i) % self.size
            if self.bit_array[digest] == False:
                return False

        return True


    @classmethod
    def get_inserts_no(self, m, p):

        n = (m * (math.log(2)**2))/(- math.log(p))
        return int(n)

    @classmethod
    def get_hash_count(self, m, n):

        k = (m/n) * math.log(2)
        return int(k)




class BloomFilter(object):

    def __init__(self, hash_count, size, fp_prob):

        # False positive probability in decimal
        self.fp_prob = fp_prob

        # Size of bit array to use
        self.size = size
        # self.size = self.get_size(items_count, fp_prob)

        # number of hash functions to use
        self.hash_count = hash_count

        # Bit array of given size
        self.bit_array = bitarray(self.size)

        # initialize all bits as 0
        self.bit_array.setall(0)

    def add(self, item):

        digests = []
        for i in range(self.hash_count):

            if i==0:
                digest = int(mmh3.hash(item, i) % (self.size/4))
                digests.append(digest)
                self.bit_array[digest] = True

            elif i==1:
                digest = int((mmh3.hash(item, i) % (self.size/4)) + self.size/4) 
                digests.append(digest)
                self.bit_array[digest] = True            
            
            elif i==2:
                digest = int((mmh3.hash(item, i) % (self.size/4)) + self.size/2)
                digests.append(digest)
                self.bit_array[digest] = True        

            elif i==3:
                digest = int((mmh3.hash(item, i) % (self.size/4)) + (self.size*(3/4)))
                digests.append(digest)
                self.bit_array[digest] = True         
    

    def check(self, item):

        for i in range(self.hash_count):
            
            if i == 0:
                digest = int(mmh3.hash(item, i) % (self.size/4))
                if self.bit_array[digest] == False:
                    return False

            elif i == 1:
                digest = int((mmh3.hash(item, i) % (self.size/4)) + self.size/4)
                if self.bit_array[digest] == False:
                    return False

            elif i == 2:
                digest = int((mmh3.hash(item, i) % (self.size/4)) + self.size/2)
                if self.bit_array[digest] == False:
                    return False

            elif i == 3:
                digest = int((mmh3.hash(item, i) % (self.size/4)) + (self.size*(3/4)))
                if self.bit_array[digest] == False:
                    return False        


        return True


    @classmethod
    def get_inserts_no(self, m, p):

        n = (m * (math.log(2)**2))/(- math.log(p))
        return int(n)

    @classmethod
    def get_hash_count(self, m, n):

        k = (m/n) * math.log(2)
        return int(k)




myBloomFilter = BloomFilterNonPartitioned(4, 2**10,0.01)

no_of_inserts = myBloomFilter.get_inserts_no(2**10, 0.01)
print(f'Calculated number of inserts: {no_of_inserts}')

myPartitionedFilter = BloomFilter(4, 2**10, 0.01)

strings1_1 = []

for i in range(no_of_inserts):
    res = "".join(random.choices(string.ascii_uppercase + string.digits, k = 8))
    strings1_1.append(res)

for i in strings1_1:
    myPartitionedFilter.add(i)

for i in strings1_1:
    myBloomFilter.add(i)

no = 0
no_part = 0
no_true = 0

for i in range(5000):
    res = "".join(random.choices(string.ascii_uppercase + string.digits, k = 8))
    no += myBloomFilter.check(res)
    no_part += myPartitionedFilter.check(res)
    if res in strings1_1:
        no_true += 1

print(f'Number of positives in non-partitioned filter: {no}')
print(f'Number of positives in partitioned filter: {no_part}')
print(f'Number of true positives: {no_true}')


false_positives = f"False positives in non-partitioned filter: {((no-no_true)/5000)*100}%"
false_positives_part = f"False positives in partitioned filter: {((no_part-no_true)/5000)*100}%"

print(false_positives)
print(false_positives_part)