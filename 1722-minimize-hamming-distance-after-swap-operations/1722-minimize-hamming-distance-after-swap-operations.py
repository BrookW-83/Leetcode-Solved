class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        n = len(target)
        par = {i: i for i in range(n)}
        rank = {i: 1 for i in range(n)}
        
        def find(n1):
            while n1 != par[n1]:
                par[n1] = par[par[n1]]
                n1 = par[n1]
            return n1
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1
            par[p2] = p1
            rank[p1] += rank[p2]
            return 1
        
        for i, j in allowedSwaps:
            union(i, j)
        
        hm = defaultdict(list)
        
        for i in range(n):
            hm[find(i)].append(i)
        
        total = 0
        
        for x in hm.values():
            s = Counter()
            t = Counter()
            
            for i in x:
                s[source[i]] += 1
                t[target[i]] += 1
        
            final = s & t
            total += sum(final.values())

        return len(source) - total