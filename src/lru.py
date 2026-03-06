from parse import read_input


def lru(k, m, requests) -> int:
    # use dictionary for lookup and storing last usage
    cache = {}

    misses = 0

    for i, r in enumerate(requests):
        # if r is in the cache, update its usage and continue
        if r in cache:
            cache[r] = i
            continue

        # else, its a miss
        misses += 1

        # if the cache isnt full, add the item to the cache
        if len(cache) < k:
            cache[r] = i
            continue

        # if the cache is full, find the item that 
        # where its been the longest since use and remove it from the cache
        item, _ = min(list(cache.items()), key=lambda x: x[1])
        
        del cache[item]

        # add the new item to the cache
        cache[r] = i

    # return the number of misses
    return misses


if __name__ == "__main__":
    # testing reading input "file1.in"
    k, m, requests = read_input("file1")
    
    # get the number of misses
    misses = lru(k, m, requests)

    print(f"{misses = }")
