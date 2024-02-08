class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] +=1
        ans=set()
        d = dict(sorted(d.items()))
        m = sorted(list(d.values()))
        print(d,m)
        for i in range(1,k+1):
            for key in d:
                if d[key]==m[-i] and key not in ans:
                    ans.add(key)
        return list(ans)
                