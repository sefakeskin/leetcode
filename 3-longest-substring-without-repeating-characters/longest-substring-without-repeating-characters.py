class Solution(object):
    def lengthOfLongestSubstring(self,sentence):
        nums=[0]
        
        def control(temp_sentence):
            used_words=[]
            for i in range(len(temp_sentence)):
                if temp_sentence[i] in used_words:
                    nums.append(i)
                    return
                used_words.append(temp_sentence[i])
            nums.append(len(temp_sentence))

        for i in range(len(sentence)):
            control(sentence[i:])            

        return max(nums)