#Problem Link: https://leetcode.com/problems/isomorphic-strings/
def isIsomorphic(s: str, t: str) -> bool:
    char_map1 = {}  #stores initial index of the mapped char of 's'
    char_map2 = {}  #stores initial index of the mapped char of 't'
    length1 = len(s)
    length2 = len(t)
    ans = True
    #Condition1: If the length of two strings are not same, then ans = False
    if length1 != length2:
        ans = False
    else:
        for i in range(length1):
            char1 = s[i]
            char2 = t[i]
            #If both characters are not mapped, map them with current index
            if (not char1 in char_map1) and (not char2 in char_map2):
                char_map1[char1] = i
                char_map2[char2] = i
            #Condition2: #If both characters are mapped and they hold different index, then ans = False
            elif (char1 in char_map1) and (char2 in char_map2):
                if char_map1[char1] != char_map2[char2]:
                        ans = False
            #Condition3: #If only one characters is mapped, then ans = False
            else:
                ans = False
    return ans          

print(isIsomorphic("babc", "baba"))     #Result : False
print(isIsomorphic("paper", "title"))     #Result : True

            
