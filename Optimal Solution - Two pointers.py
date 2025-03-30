'''
Algorithm(Main function):-

  Initialize left pointer to 0 and right pointer to len(s) - 1.
  While left pointer is less than right pointer:
  a. If the characters at the left and right pointers are not equal:
    i. Check if deleting the character at the left pointer makes the rest of the string a palindrome by calling the isPalindrome method with left pointer incremented by 1 and right pointer.
       If it returns True, return True from the method.
    ii. Check if deleting the character at the right pointer makes the rest of the string a palindrome by calling the isPalindrome method with left pointer and right pointer decremented by 1.
        If it returns True, return True from the method.
    iii. Otherwise, both substrings are not palindromes, return False.
  b. Otherwise, characters at the left and right pointers are equal, increment left pointer and decrement right pointer.
      If the method hasn't returned True yet, it means the string is a palindrome, return True.

Algorithm for the isPalindrome method:
  While left pointer is less than right pointer:
  a. If the characters at the left and right pointers are not equal, return False.
  b. Otherwise, increment left pointer and decrement right pointer.
  If the method hasn't returned False yet, it means the string is a palindrome, return True.
'''

def validPalindrome(self, s) :   #You should ignore the self parameter if you do not refer to any class instances guys, remember that.
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Check if deleting the left character makes the rest of the string a palindrome
                if self.isPalindrome(s, left + 1, right):   #You should ignore the self parameter if you do not refer to any class function guys, remember that.
                    return True
                # Check if deleting the right character makes the rest of the string a palindrome
                elif self.isPalindrome(s, left, right - 1):
                    return True
                else:
                    # Both substrings are not palindromes
                    return False
            left += 1
            right -= 1
        return True
    
def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
