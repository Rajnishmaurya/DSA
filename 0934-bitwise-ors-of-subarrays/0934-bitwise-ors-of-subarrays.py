class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        unique=set()
        prev=set()

        for num in arr:
            p=set()
            unique.add(num)
            p.add(num)
            for temp in prev:
                x=temp | num
                unique.add(x)
                p.add(x)
            prev=p
        return len(unique)
"""
Intuition
To count all distinct bitwise OR results from subarrays, we process each number and track all OR results from subarrays ending at that index. For each element, we:

Start a new subarray with the current number.
Extend previous subarrays by OR-ing with the current number.
Because the OR operation is monotonic, the number of distinct results at each step is limited—OR-ing more elements can't undo bits already set—so the total number of unique values grows slowly.

Complexity
Time complexity: O(n * 32)
At each index, we OR the current number with previous OR results.
The number of distinct OR values per step is bounded by the number of bits in the integers.
The maximum number in the array is ≤ 10⁹ → fits in 30 bits.
So we can generate at most 32 distinct OR results per index (worst case).
Total work: n * 32.
Space complexity: O(n)
"""