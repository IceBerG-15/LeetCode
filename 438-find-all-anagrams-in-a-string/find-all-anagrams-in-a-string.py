class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)

        if s_len < p_len:
            return []

        freq_p = [0 for _ in range(26)]
        window = [0 for _ in range(26)]

        for i in range(p_len):
            window[ord(s[i])-ord('a')] += 1
            freq_p[ord(p[i])-ord('a')] += 1

        ans = []
        if freq_p == window:
            ans.append(0)
        
        for i in range(p_len,s_len):
            window[ord(s[i-p_len]) - ord('a')] -= 1
            window[ord(s[i])-ord('a')] += 1
            if window == freq_p:
                ans.append(i-p_len+1)
        return ans