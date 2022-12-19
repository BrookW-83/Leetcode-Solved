class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        s[].lower()  #change all the string to lower case
        s[].isalnum() #check for alphanumeric characters
        l, r = 0, len(s)-1
        if s[r] == s[i]
            return True
        else:
            return False
         #if the left and right alpahnumeric characters are the same return True    
          else False
        """

        l , r = 0, len(s)-1

        while l <= r :
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True