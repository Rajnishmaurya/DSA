class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        unique = set()
        prev = set()

        for num in arr:
            p = set([num])
            unique.add(num)
            for num1 in prev:
                curr = num1 | num
                unique.add(curr)
                p.add(curr)
            prev = p
        
        return len(unique)
        