class TrieNode:
    def __init__(self):
        self.child=[None,None]

class Solution:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,x):
        t=self.root

        for i in range(31,-1,-1):
            bit=(x>>i) & 1
            if not t.child[bit]:
                t.child[bit]=TrieNode()
            t=t.child[bit]

    def maximum(self,x):
        t=self.root
        answer=0

        for i in range(31,-1,-1):
            bit=(x>>i)&1
            opposite_bit=1-bit
            if t.child[opposite_bit]:
                answer+=(1<<i)
                t=t.child[opposite_bit]
            else:
                t=t.child[bit]
        
        return answer
    

    def findMaximumXOR(self, nums: List[int]) -> int:

        for num in nums:
            self.insert(num)

        answer=0

        for num in nums:
            answer=max(answer,self.maximum(num))
        return answer
        