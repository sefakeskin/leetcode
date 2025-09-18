class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp=x
        reverse=0
        
        while temp>0:
            reverse=reverse*10
            reverse+=temp%10
            temp=int(temp/10)

        if x==reverse:
            return True
        else:
            return False