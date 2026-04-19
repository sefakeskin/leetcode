class Solution:
    def reverse(self,x: int) -> int:
        if x>0:
            x_string=str(x)
            reverse_x_string=x_string[::-1]
            reverse_x=int(reverse_x_string)
            if reverse_x<=2**31-1 and reverse_x>=-2**31:
                return reverse_x
            else:
                return 0
        else:
            x=abs(x)
            x_string=str(x)
            reverse_x_string=x_string[::-1]
            reverse_x=-int(reverse_x_string)
            if reverse_x<=2**31-1 and reverse_x>=-2**31:
                return reverse_x
            else:
                return 0            

            