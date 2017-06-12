class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = s.split(' ')
        reverse = []
        for word in temp:
            reverse_word = word[::-1]
            reverse.append(reverse_word)
        return (' '.join(reverse))
if __name__ == '__main__':
    s = Solution()
    string = "Let's take LeetCode contest"
    result = s.reverseWords(string)
    print(result)