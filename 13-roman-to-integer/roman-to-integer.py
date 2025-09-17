class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        SymboltoValue={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        value=0
        flag=0
        for curr_letter,next_letter in zip(s,s[1:]):
            if flag==1:
                flag=0
                continue
            
            if curr_letter=="I":
                if next_letter=="V":
                    value+=4
                    flag=1
                    continue
                elif next_letter=="X":
                    value+=9
                    flag=1
                    continue
            
            if curr_letter=="X":
                if next_letter=="L":
                    value+=40
                    flag=1
                    continue
                elif next_letter=="C":
                    value+=90
                    flag=1
                    continue
            if curr_letter=="C":
                if next_letter=="D":
                    value+=400
                    flag=1
                    continue
                elif next_letter=="M":
                    value+=900
                    flag=1
                    continue
            
            value+=SymboltoValue[curr_letter]

        if len(s)==1:
            value+=SymboltoValue[s]

        elif len(s)>1:
            if s[-2]=="C" and (s[-1]=="D" or s[-1]=="M"):
                pass 
            elif s[-2]=="I" and (s[-1]=="V" or s[-1]=="X"):
                pass
            elif s[-2]=="X" and (s[-1]=="L" or s[-1]=="C"):
                pass
            else:
                value+=SymboltoValue[s[-1]]
        
        return value

