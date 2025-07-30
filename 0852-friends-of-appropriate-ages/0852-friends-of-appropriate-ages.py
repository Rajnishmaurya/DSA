class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count=0

        count_by_age=Counter(ages)

        for age_a in range(1,121):
            for age_b in range(1,121):
                if age_b<=0.5*age_a+7:
                    continue
                if age_b > age_a:
                    continue
                if age_b > 100 and age_a <100:
                    continue
                count_a=count_by_age[age_a]
                count_b=count_by_age[age_b]

                if age_a==age_b:
                    count+=count_a*(count_a-1)
                else:
                    count+=count_a*count_b
        return count

        return count
        