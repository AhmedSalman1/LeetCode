class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        min_heap = []
        for word, freq in counter.items():
            heapq.heappush(min_heap, (-freq, word))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        
        return res