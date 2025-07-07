from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        dists = []
        
        dists.append((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        dists.append((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2)
        dists.append((p1[0] - p4[0])**2 + (p1[1] - p4[1])**2)
        dists.append((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2)
        dists.append((p2[0] - p4[0])**2 + (p2[1] - p4[1])**2)
        dists.append((p3[0] - p4[0])**2 + (p3[1] - p4[1])**2)
        
        dists.sort()

        for i in range(1, 4):
            if dists[i - 1] != dists[i]:
                return False
        if dists[0] == 0:
            return False


        if dists[4] != dists[5]:
            return False

        if dists[4] != 2 * dists[0]:
            return False

        return True
