
# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# First solution :
# On itère sur la liste pour compter le nombre d'apparition de chaque élément, puis on trie les éléments en fonction de leur nombre d'apparition et on retourne les k premiers éléments.

from collections import defaultdict
from typing import List

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    hash = defaultdict(int)
    for n in nums :
        hash[n] += 1
    return [x[0] for x in sorted(hash.items(), key=lambda x : x[1], reverse=True)[:k]]

# Time complexity : O(n log n) where n is the number of elements in the array. We go through the array once to count the frequency and then we sort the elements based on their frequency.
# Space complexity : O(n) We store all the elements in the hashmap.

# Second solution :
# On utilise un heap pour stocker les éléments en fonction de leur fréquence. On parcourt la liste pour compter le nombre d'apparition de chaque élément, puis on ajoute les éléments dans le heap en fonction de leur fréquence. 
# Enfin, on retourne les k éléments les plus fréquents.

import heapq

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    hash = defaultdict(int)
    for n in nums :
        hash[n] += 1
    heap = []
    for key, value in hash.items() :
        heapq.heappush(heap, (-value, key))
    return [heapq.heappop(heap)[1] for _ in range(k)]

# Time complexity : O(n log k) where n is the number of elements in the array. We go through the array once to count the frequency and then we add the elements to the heap which takes O(log k) time.
# Space complexity : O(n) We store all the elements in the hashmap and the heap.

# Third solution :
# We use bicket sort to sort the elements based on their frequency. We create a list of buckets where the index of the bucket represents the frequency of the elements. 
# We iterate through the list to count the frequency of each element and add them to the corresponding bucket. 
# Finally, we iterate through the buckets in reverse order to get the k most frequent elements.

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    hash = defaultdict(int)
    for n in nums :
        hash[n] += 1
    buckets = [[] for _ in range(len(nums) + 1)]
    for key, value in hash.items() :
        buckets[value].append(key)
    res = []
    for i in range(len(buckets) - 1, 0, -1) :
        for n in buckets[i] :
            res.append(n)
            if len(res) == k :
                return res
            
# Time complexity : O(n) where n is the number of elements in the array. We go through the array once to count the frequency and then we go through the buckets to get the k most frequent elements.
# Space complexity : O(n) We store all the elements in the hashmap and the buckets.