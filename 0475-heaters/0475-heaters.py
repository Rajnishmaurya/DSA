class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        '''For every house, find the nearest heater distance. The largest among these distances will be our answer.
We can use Binary Search using the bisect module in python to find the suitable index from the heaters array.
We have 3 cases for every house- If a house is to the left of the first heater, if a house is the the right of the last heater, if a house is in between two heaters.'''
        houses.sort()
        heaters.sort()

        ans=0

        for house in houses:
            index=bisect.bisect_left(heaters,house)

            if index==0:
                nearest=heaters[0]-house
            elif index==len(heaters):
                nearest=house-heaters[-1]
            else:
                nearest=min(heaters[index]-house,house-heaters[index-1])
            ans=max(ans,nearest)
        return ans
            



        