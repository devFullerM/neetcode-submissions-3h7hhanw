class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_count = {}
        window_count = {}

        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        have = 0
        need = len(t_count)
        l = 0

        min_length = float("inf")
        result = [-1, -1]

        for r in range(len(s)):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < min_length:
                    result = [l, r]
                    min_length = r - l + 1

                window_count[s[l]] -= 1

                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1

                l += 1
        l, r = result
        return s[l:r + 1] if min_length != float("inf") else ""

