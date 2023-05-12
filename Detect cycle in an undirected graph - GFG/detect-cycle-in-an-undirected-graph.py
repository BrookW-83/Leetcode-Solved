from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		inDegree = [0] * V
		for i in range(V):
		    inDegree[i] = len(adj[i])
		    
		q = deque()
		for i in range(V):
		    if inDegree[i] <= 1:
		        q.append(i)
	    path = []      
		while q:
		    num = q.popleft()
		    path.append(num)
		    for child in adj[num]:
		        inDegree[child] -= 1
		        if inDegree[child] == 1:
		            q.append(child)
		        
		        
        return len(path) != V


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends