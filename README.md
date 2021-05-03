## Running project:

- clone the repository
- install dependecies
- run python3 filename.py

## I Hash tables:

| Load factor / HT size |                     | 2^10                  | 2^14                  | 2^18                  |
| --------------------- | ------------------- | --------------------- | --------------------- | --------------------- |
| 0.5                   | Min query time:     | 1.3389 * 10^-6 s      | 1.335 * 10^-6 s     | 1.344 * 10^-6 s             |
|                       | Max query time:     | 42.3389 * 10^-6 s     | 42.694 * 10^-6 s     | 69.414 * 10^-6 s     |
|                       | Average query time: | 1.795 * 10^-6 s   | 1.806 * 10^-6 s | 1.917 * 10^-6 s |
| 0.75                  | Min query time:     | 1.3239 * 10^-6 s | 1.307 * 10^-6 s | 1.339 * 10^-6 s |
|                       | Max query time:     | 62.5019 * 10^-6 s  | 41.289 * 10^-6 s  | 71.848 * 10^-6 s    |
|                       | Average query time: | 2.074 * 10^-6 s  | 2.088 * 10^-6 s  | 2.282 * 10^-6 s |
| 0.95                  | Min query time:     | 1.3239 * 10^-6 s| 1.324 * 10^-6 s | 1.354 * 10^-6 s |
|                       | Max query time:     | 1602.42 * 10^-6 s   | 3438.38 * 10^-6 s      |  7554.74 * 10^-6 s    |
|                       | Average query time: | 3.46 * 10^-6 s | 3.975 * 10^-6 s  | 4.363 * 10^-6 s  |


Given this info, and running this demo on our own, we can conclude that average query time is independent of hash table size, and depends exclusively on load factor. I digged down the C implementation of Python dictionary data structure, and found that for this exact reason, upon filling half of allocated memory, C compiler dubles the size of hash table and rehashes all entries. 
<br/>
<br/>

## II Bloom filters:

- m = 2^10, k = 4 -> **n = 106** for p = 1%
- m = 2^12, k = 4 -> **n = 427** for p = 1%
- m = 2^16, k = 4 -> **n = 6837** for p = 1%

<br/>

**TABLE: False positive table:**
| Type of BF / Size | 2^10 | 2^12 | 2^16 |
| ----------------- | ---- | ---- | ---- |
| Non-partitioned BF | 1.119% | 1.08% | 1.3% |
| Partitioned BF | 1.559% | 1.42% | 1.42% |

<br/>

### Discussion:
Given this info, and running this demo on our own, we can conclude that Partitioned Bloom Filter give slightly worse False Positive rate on average. In literature I found that it is to be expected. Again there is no clear difference between Bloom Filter sizes, which is to be expected because we calculated number of entries to be proportional to Bloom filter size. 

<br/>
<br/>
