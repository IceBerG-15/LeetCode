class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s1_len = len(s)
        s2_len = len(p)

        if s1_len < s2_len:
            return []

        freq_p = [0 for _ in range(26)]
        window = [0 for _ in range(26)]

        for i in range(s2_len):
            window[ord(s[i])-ord('a')] += 1
            freq_p[ord(p[i])-ord('a')] += 1

        ans = []
        if freq_p == window:
            ans.append(0)
        
        for i in range(s2_len,s1_len):
            window[ord(s[i-s2_len]) - ord('a')] -= 1
            window[ord(s[i])-ord('a')] += 1
            if window == freq_p:
                ans.append(i-s2_len+1)
        return ans