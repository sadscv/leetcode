class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candies = sorted(candies)
        prev = -1
        count = 0
        for c in candies:
            if c != prev:
                count += 1
                prev = c
        return count if count < len(candies)//2 else len(candies)//2
if __name__ == '__main__':
    s = Solution()
    candies = [1,1,2,3]
    result = s.distributeCandies(candies)
    print(result)