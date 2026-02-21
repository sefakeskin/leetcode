class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_length = min(len(word) for word in strs)
        longest_prefix=[]
        for i in range(min_length): 
            letters = [word[i] for word in strs]

            if min(letters)==max(letters):
                longest_prefix.append(letters[0])
            else:
                break
        longest_prefix = "".join(longest_prefix)


        return longest_prefix
