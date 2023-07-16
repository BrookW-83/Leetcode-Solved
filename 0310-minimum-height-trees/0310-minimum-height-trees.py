class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = {i: set() for i in range(n)}
        for e1, e2 in edges:
            graph[e1].add(e2)
            graph[e2].add(e1)
            
        leaf = [i for i in range(n) if len(graph[i]) == 1]

        while n > 2:
            n -= len(leaf)
            new_leaf = []
            for i in leaf:
                neighbor = graph[i].pop()
                graph[neighbor].remove(i)


                if len(graph[neighbor]) == 1:
                    new_leaf.append(neighbor)


            leaf = new_leaf

        return leaf


