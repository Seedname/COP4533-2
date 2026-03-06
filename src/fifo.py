from parse import read_input
from collections import deque


def fifo(k, m, requests) -> int:
    # use a cache for quick lookups
    cache = set()

    # use a queue to determine which item to evict
    eviction = deque(maxlen=k)

    misses = 0

    for r in requests:
        # if r is in the cache, continue
        if r in cache:
            continue

        # else, its a miss
        misses += 1

        # if the cache isnt full, add the item to the cache
        if len(cache) < k:
            cache.add(r)
            eviction.append(r)
            continue

        # if the cache is full, first evict the oldest item
        item = eviction.popleft()

        # remove it from the cache
        cache.remove(item)

        # add the new request to the cache
        cache.add(r)
        eviction.append(r)

    # return the number of misses
    return misses


if __name__ == "__main__":
    # testing reading input "file1.in"
    k, m, requests = read_input("file1")
    
    # get the number of misses
    misses = fifo(k, m, requests)

    print(f"{misses = }")
