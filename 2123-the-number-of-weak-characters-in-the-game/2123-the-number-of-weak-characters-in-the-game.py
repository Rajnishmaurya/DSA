class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:(x[0],-x[1]))
        n=len(properties)
        answer=0
        mini=-1
        for i in range(n-1,-1,-1):
            if properties[i][1]<mini:
                answer+=1
            else:
                mini=properties[i][1]
        return answer



        