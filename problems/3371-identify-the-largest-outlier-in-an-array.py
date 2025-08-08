# LeetCode 3371 - Identify the Largest Outlier in an Array
# https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        freq = collections.Counter(nums)
        ans = None

        # considering x == outlier 
        for x in nums:
            # remaining sum
            T = total - x
            if T % 2 != 0:
                # x is not the outlier if the remaing sum is odd
                # b/c remainin sum has to be T = y * 2
                continue
            # y = sum of all special numbers
            y = T //2 

            # remove x temporarily 
            freq[x] -= 1
            # y must exist among the remaining nubmers 
            if freq[y] > 0 :
                if ans is None or x > ans: 
                    # checking for the largest outlier
                    if ans is None or x > ans: 
                        ans = x
            
            #restore
            freq[x] += 1 
        
        # prob guarantees at least one valid outlier
        return ans if ans is not None else 0