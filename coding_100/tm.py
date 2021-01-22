#'abcba'

s = 'abccb'
global rst 
rst= 0 

def longest_str(s):
    ''' 返回最长回文子串的长度'''
    global rst
    if len(s) == 1:
        return 1 
    start = 0 
    end = len(s) -1 
    
    while start < end:
        if s[start] == s[end]:
            rst += 2 
            start += 1
            end -= 1
        else:
            rst = 0 
            return max(longest_str(s[start+1:]) , longest_str(s[:end-1]))

    return rst 


print(longest_str(s))
''' 要将最长的子串返回，最好返回的是子串的index'''

dp = [[ 0 for _ in range(len(s)) ] for _ in range(len(s))]

def longest_str(s):
    ''' 返回最长的回文子串'''
    if len(s) == 1:
        return s
    start  = 0 
    end = len(s) -1 
    
    
    
