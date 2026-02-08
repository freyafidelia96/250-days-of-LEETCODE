def topKfrequent(nums, k):
    from collections import Counter
    """import heapq

    # Count the frequency of each element in nums
    count = Counter(nums)
    
    # Use a heap to find the k most common elements
    return [item for item, freq in heapq.nlargest(k, count.items(), key=lambda x: x[1])]"""
    
    """count = Counter(nums)
    

    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_count[:k]]
"""
    freq = [[] for i in range(len(nums) + 1)]
    
    for num, count in count.items():
        freq[count].append(num)
        
    res = []
    
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    
    

if __name__ == "__main__":
    print(topKfrequent([1,1,1,2,2,3], 2))  # Expected: [1, 2]
    print(topKfrequent([1], 1))              # Expected: [1]
    
    
    