class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for c in range(len(s)):

            if len(st) == 0:
                st.append(s[c])

            elif (
                s[c] == '}' and st[-1] == '{' or
                s[c] == ')' and st[-1] == '(' or
                s[c] == ']' and st[-1] == '['
            ):
                st.pop()

            else:
                st.append(s[c])

        return len(st) == 0