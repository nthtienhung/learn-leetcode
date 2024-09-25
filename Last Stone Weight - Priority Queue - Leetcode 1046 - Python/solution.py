class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #why -? what is this loop syntax
        stones = [-s for s in stones]
        #no need to declare heapq first?
        #what is heap?
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        #why 0
        stones.append(0)
        return abs(stones[0])