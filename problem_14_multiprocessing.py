import sys

sys.setrecursionlimit(10000)

import numpy as np
import multiprocessing as mp

from functools import reduce

def get_next_step(original, data, depth, output):
    depth += 1
    mask_even = (data & 1) == 0
    mask_odd = ~mask_even
    
    data[mask_even] = data[mask_even]/2
    data[mask_odd] = 3*data[mask_odd] + 1
    
    mask_one = (data != 1)
    mask_sum = np.sum(mask_one)
    
    if mask_sum != 1:
        get_next_step(original[mask_one], data[mask_one], depth, output)
    else:
        output.put((depth, original[mask_one][0]))


from time import time

if __name__ ==  '__main__':
    start = time()

    tries = np.arange(1, int(1e6), dtype=np.int64)
    np.random.shuffle(tries)

    N = 2

    splits = (np.arange(1, N) * len(tries)/N).astype(int)
    tries = np.split(tries, splits)

    output = mp.Queue()
    processes = []
    for data_i in tries:
        p = mp.Process(target=get_next_step, args=(data_i, 1*data_i, 0, output))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    results = [output.get() for p in processes]
    results.sort()
    print(f'Loop depth, number: {results[-1]}')
    print(f'time = {time()-start}')
    
    # 2.5 s on 2 cores