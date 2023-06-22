class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        rec = defaultdict(int)
        graph = defaultdict(list)
        
        for recipe, inc in zip(recipes, ingredients):
            for i in inc:
                graph[i].append(recipe)
                rec[recipe] += 1
        
        for supply in supplies:
            if supply in graph:
                for recipe in graph[supply]:
                    rec[recipe] -= 1
         
        q = deque()
        for recipe, num_parents in rec.items():
            if num_parents == 0:
                q.append(recipe)
                
        ans = []
        while q:
            current = q.popleft()
            ans.append(current)    
            for child in graph[current]:
                rec[child] -= 1
                if rec[child] == 0:
                    q.append(child)
                    
        return ans
        