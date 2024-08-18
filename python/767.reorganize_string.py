from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        # Grab all the chars in the string
        # Count all the chars using counter
        # Insert to string by order of 1. not same as before 2. highest count. 3. alphabetically 
        # Optimize further by following all possible combos
        if len(s) == 0 or s == '':
            return ''
        counts = Counter(s)
        res = ''

        while counts:
            most_common = counts.most_common()
            length = len(res)
            
            for char, count in most_common:
                if len(res) == 0 or char != res[-1]:
                    res += char
                    counts[char] -= 1
                    if counts[char] == 0:
                        del counts[char]
                    break
            
            if len(res) == length:
                return '' 
        return res


        
        
             
