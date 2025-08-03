class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        dq=deque()
        dq.append(x)

        steps=0
        visited=set()

        while dq:
            n=len(dq)

            for _ in range(n):
                item=dq.popleft()
                if item==y:
                    return steps
                visited.add(item)
                if item%11==0 and item//11 not in visited:
                    dq.append(item//11)
                if item%5==0 and item//5 not in visited:
                    dq.append(item//5)
                if item+1 not in visited:
                    dq.append(item+1)
                if item-1 not in visited:
                    dq.append(item-1)
            steps+=1
        return -1
        