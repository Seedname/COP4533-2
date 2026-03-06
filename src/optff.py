from parse import read_input
import heapq


def optff(k, m, requests) -> int:
    # initialize cache, misses, and heap for determining which item to evict
    cache = set()
    misses = 0
    max_heap = []
    
    # initialize index map and next_occurrence array to track which is furthest in the future
    index_map = {}
    next_occurrence = [float('inf')] * len(requests)
    
    # populate the next_occurrence array with the index of the next occurrence of each request
    for i in range(len(requests)-1, -1, -1):
        if requests[i] in index_map:
            next_occurrence[i] = index_map[requests[i]]
        index_map[requests[i]] = i
    
    for i in range(len(requests)):
        # if the item is already in the cache, push it onto the heap with its next occurrence
        if requests[i] in cache:
            heapq.heappush(max_heap, (-next_occurrence[i], requests[i]))
        # if the cache is not full, add the item to the cache and push it onto the heap
        elif len(cache) < k:
            cache.add(requests[i])
            heapq.heappush(max_heap, (-next_occurrence[i], requests[i]))
            misses += 1
        # if the cache is full and the item is not in the cache, evict the item that is furthest in the future
        else:
            eviction = heapq.heappop(max_heap)[1]
            while eviction not in cache:
                eviction = heapq.heappop(max_heap)[1]
            cache.remove(eviction)
            cache.add(requests[i])
            heapq.heappush(max_heap, (-next_occurrence[i], requests[i]))
            misses += 1
            
    return misses


if __name__ == "__main__":
    # testing reading input "file1.in"
    k, m, requests = read_input("file1")
    
    # get the number of misses
    misses = optff(k, m, requests)

    print(f"{misses = }")