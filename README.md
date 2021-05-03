## Running project:

- clone the repository
- install dependecies
- run python3 filename.py

## Hash tables:

| Load factor / HT size |                     | 2^10                  | 2^14                  | 2^18                  |
| --------------------- | ------------------- | --------------------- | --------------------- | --------------------- |
| 0.5                   | Min query time:     | 1.3389 * 10^-6 s      | 1.335 * 10^-6 s     | 1.795 * 10^-6 s             |
|                       | Max query time:     | 42.3389 * 10^-6 s     | 42.694 * 10^-6 s     | 2.074 * 10^-6 s     |
|                       | Average query time: | 1.795 * 10^-6 s   | 1.806 * 10^-6 s | 0.0007189389962150017 |
| 0.75                  | Min query time:     | 1.3239 * 10^-6 s | 1.307 * 10^-6 s | 0.0004999637603759766 |
|                       | Max query time:     | 62.5019 * 10^-6 s  | 41.289 * 10^-6 s  | 14.280799984931946    |
|                       | Average query time: | 2.074 * 10^-6 s  | 2.088 * 10^-6 s  | 0.0007933307806524681 |
| 0.95                  | Min query time:     | 1.3239 * 10^-6 s| 0.0004999637603759766 | 0.0004999637603759766 |
|                       | Max query time:     | 1602.42 * 10^-6 s   | 1.76910001039505      | 11.653299987316132    |
|                       | Average query time: | 0.0015998961746631398 | 0.006240295617097143  | 0.030601435926947515  |

<br/>
<br/>

### II Bloom filters:

**Number of inserts that makes the original Bloom filter have the false positive rate f=1%:**

- m = 2^10, k = 4 -> **n = 98** for p = 1%
- m = 2^12, k = 4 -> **n = 390** for p = 1%
- m = 2^16, k = 4 -> **n = 6229** for p = 1%

<br/>

**TABLE 1: False positive rates table:**
| Type of BF / Size | 2^10 | 2^12 | 2^16 |
| ----------------- | ---- | ---- | ---- |
| Original BF | 93.66% | 14.29% | 0% |
| Partitioned BF | 92.84% | 15.64% | 0% |

<br/>

### Discussion:

If we calculate probability of a false positives we will get these results

**TABLE 2: Probability of a false positives table: (n = 1000, k = 4)**
| | 2^10 | 2^12 | 2^16 |
| ----------------- | ---- | ---- | ---- |
| False positive rate: | 92.19% | 15.10% | 0% |

<br/>

By analyzing the False positive rates from the Table 1 and the Table 2 it can be clearly seen that both of the bloom filters perform as expected. Furthermore on the Table 1 we can see that the results are not so different between the two Bloom filters. Both bloom filters perform very well (0% false positive rate) if we allocate enough space (m) and will perform very bad (which is expected) if the allocated space (m) is not enough for the number of items that will be inserted.

Now what is interesting to see is that by increasing number of hash functions we will get worse values for the false positive rates.

**TABLE 3: False positive rates table: (k = 6)**
| Type of BF / Size | 2^10 | 2^12 | 2^16 |
| ----------------- | ---- | ---- | ---- |
| Original BF | 98.1% | 19.42% | 0% |
| Partitioned BF | 98.82% | 19.96% | 0% |

<br/>
<br/>
