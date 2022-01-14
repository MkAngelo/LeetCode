class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        long_prefix = ''
        if len(strs) == 0 or strs[0] == '': return long_prefix
        ind = 0
        l = len(strs[0])
        lon = 0
        while ind <= l:
            try: 
                temp = strs[0][ind]

                for i in range(len(strs)):          
                    if strs[i][ind] != temp:
                        return long_prefix
                ind+=1
                lon += 1
                long_prefix += temp
            except:
                return long_prefix
        return long_prefix
