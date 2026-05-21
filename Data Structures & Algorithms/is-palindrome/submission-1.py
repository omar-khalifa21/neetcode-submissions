class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        7 "abc cba" -> True
        5 "abcba" -> True
        4 "abba" -> True
        """
        
        s_length: int = len(s)

        if s_length <= 1:
            return True

        left_pointer = 0
        right_pointer = s_length - 1

        while left_pointer < right_pointer:
            if not s[left_pointer].isalnum():
                left_pointer += 1
                continue
            
            if not s[right_pointer].isalnum():
                right_pointer -= 1
                continue


            if s[left_pointer].lower() != s[right_pointer].lower():
                print(f"left_pointer: {left_pointer}, right_pointer: {right_pointer}, {s[left_pointer], s[right_pointer]}")
                return False
            left_pointer += 1
            right_pointer -= 1

        return True
        
        