class Solution(object):
    def getreverse(self,s):
            return s[::-1]
                

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        for will_check in range(len(s),0,-1):
            
            tour=len(s)-will_check+1
            for i in range(tour):
                string_will_check=s[i:i+will_check]
                if string_will_check==self.getreverse(string_will_check):
                    return string_will_check
                

            