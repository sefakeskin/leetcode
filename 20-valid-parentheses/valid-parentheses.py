class Solution:
    def isValid(self, s: str) -> bool:
        my_stack=[]
        parantheses=list(s)
        map_parantheses = {")": "(", "}": "{", "]": "["}

        for i in parantheses:

            if my_stack and i in map_parantheses and my_stack[-1]==map_parantheses[i]:
                my_stack.pop()
            else:
                my_stack.append(i)
        
        if len(my_stack)==0:
            return True
        else:
            return False
        