class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        keys=set(bannedWords)

        result=0
        for word in message:
            if word in keys:
                result+=1
        
        if result>1:
            return True
        else:
            return False
        