import os, sys, string, random, time

#setting seed to 0, so hashes are constant
hashseed = os.getenv('PYTHONHASHSEED')
if not hashseed:
    os.environ['PYTHONHASHSEED'] = '0'
    os.execv(sys.executable, [sys.executable] + sys.argv)



#my simple implementation of hashtable with linear probing
class hash_table:

    def __init__(self, size):
        self.size = size
        self.list = [None for i in range(self.size)]

    def insert(self, value):
        self.hash = hash(value)
        index = self.hash%self.size
        if self.list[index] == None:
            self.list[index] = value

        else:
            while self.list[index] != None:
                index += 1
                if index == self.size:
                    index = 0

            self.list[index] = value

    def lookup(self, value):
        self.hash = hash(value)
        index = self.hash%self.size

        if self.list[index] == value:
            return(self.list[index])

        else:
            while self.list[index] != value:
                index += 1
                if index == self.size:
                    index = 0
                if self.list[index] == None:
                    break

            if self.list[index] != None:
                return(self.list[index])


size = 2**14

h1_1 = hash_table(size)
load_factor1 = int(size * 0.5)
strings1_1 = []
for i in range(load_factor1):
    res = "".join(random.choices(string.ascii_uppercase + string.digits, k = 8))
    h1_1.insert(res)
    strings1_1.append(res)

exectime1_1 = []
for i in range(2**20):
    val = strings1_1[random.randint(0, load_factor1-1)]
    t = time.process_time()
    h1_1.lookup(val)
    elapsed_time = time.process_time() - t
    exectime1_1.append(elapsed_time)

print("Execution time, loadfactor = 0.5")
print(f"min = {min(exectime1_1)}")
print(f"max = {max(exectime1_1)}")
print(f"aver = {sum(exectime1_1)/len(exectime1_1)}")


h1_2 = hash_table(size)
load_factor2 = int(size * 0.75)
strings1_2 = []
for i in range(load_factor2):
    res = "".join(random.choices(string.ascii_uppercase + string.digits, k = 8))
    h1_2.insert(res)
    strings1_2.append(res)

exectime1_2 = []
for i in range(2**20):
    val = strings1_2[random.randint(0, load_factor2-1)]
    t = time.process_time()
    h1_2.lookup(val)
    elapsed_time = time.process_time() - t
    exectime1_2.append(elapsed_time)

print("\nExecution time, loadfactor = 0.75")
print(f"min = {min(exectime1_2)}")
print(f"max = {max(exectime1_2)}")
print(f"aver = {sum(exectime1_2)/len(exectime1_2)}")


h1_3 = hash_table(size)
load_factor3 = int(size * 0.95)
strings1_3 = []
for i in range(load_factor3):
    res = "".join(random.choices(string.ascii_uppercase + string.digits, k = 8))
    h1_3.insert(res)
    strings1_3.append(res)

exectime1_3 = []
for i in range(2**20):
    val = strings1_3[random.randint(0, load_factor3-1)]
    t = time.process_time()
    h1_3.lookup(val)
    elapsed_time = time.process_time() - t
    exectime1_3.append(elapsed_time)

print("\nExecution time, loadfactor = 0.95")
print(f"min = {min(exectime1_3)}")
print(f"max = {max(exectime1_3)}")
print(f"aver = {sum(exectime1_3)/len(exectime1_3)}")
