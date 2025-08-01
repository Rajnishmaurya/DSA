class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        result=[]
        if len(changed)%2!=0:
            return result

        changed.sort()
        count=Counter(changed)
        
        if count[0]%2!=0:
            return result

        for element in changed:
            if count[element]==0: # for double element
                continue
            if count[2*element]==0:
                return []
            result.append(element)
            count[element]-=1
            count[2*element]-=1
        return result
            