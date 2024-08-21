#Problem Link: https://leetcode.com/problems/isomorphic-strings/

def isIsomorphic(s, t):
    dummy_string = ""       # to create the replaced string
    char_dictionary = {}    # for storing char mapping
    char_set = []           # to store the mapped characters of string t
    #If the lengths of string_1 and string_2 are not similar return false
    if len(s)!=len(t):
        return False
    else:
        for i in range(len(s)):
            char = s[i]
            #if the char is not stored in dictionary
            if not char in char_dictionary:
                mapped_char = t[i]
                # and the pointed character of string t is not mapped  
                if not mapped_char in char_set:
                    char_dictionary[char] = mapped_char     #map the characters
                    char_set.append(mapped_char)            #store the mapped characters of string t
                    dummy_string = dummy_string + char_dictionary[char]
                else:
                    return False
            else:
                dummy_string = dummy_string + char_dictionary[char]
        #If the for loop runs successfully and the replaced string == t, then return true
        if dummy_string == t:
            return True
        else: 
            return False       
        

print(isIsomorphic("babc", "baba"))     #Result : False
print(isIsomorphic("paper", "title"))     #Result : True

            