class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        list = [column for row in nums for column in row]
        if c * r != len(list):
            return nums
        else:
            temp = []
            count = 0
            for rows in range(r):
                left, list = list[:c], list[c:]
                temp.append(left)
            return temp

if __name__ == '__main__':
    solution = Solution()
    nums = [[1, 2],[3, 4]]
    r = 2
    c = 2
    result = solution.matrixReshape(nums, r, c)
    print(result)