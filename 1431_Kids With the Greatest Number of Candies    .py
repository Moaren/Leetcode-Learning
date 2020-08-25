# TAKEAWAY:
# 1. Can try to reduce memory usage by use the input list as the output one
# 2. get_max is different and much easier than SORT!!!!!
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        def get_max(lis):
            result = None
            for i in lis:
                if result == None:
                    result = i
                else:
                    if result < i:
                        result = i
            return result
        
        max_candy = get_max(candies)
        for index in range(len(candies)):
            candies[index] = bool(max_candy - candies[index] <= extraCandies)
        return candies