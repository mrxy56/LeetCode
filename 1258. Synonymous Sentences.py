class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        ind = {}
        index = 0
        
        for pair in synonyms:
            for word in pair:
                if word not in ind:
                    ind[word] = index
                    index += 1
        
        text = text.split()
        
        for word in text:        # build the dictionary
            if word not in ind:
                ind[word] = index
                index += 1
                
        parent = [i for i in range(len(ind))]
        
        def find(a):
            if a != parent[a]:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a, b): # union_find
            parent[find(b)] = find(a)
        
        for x, y in synonyms:
            union(ind[x], ind[y])
        
        def dfs(i): # backtracking
            if i == len(text):
                return [""]
            root = find(ind[text[i]])
            possibles = []
            for k, v in ind.items():
                if find(v) == root:
                    possibles.append(k)
            res = []
            for w in possibles:
                new_texts = dfs(i + 1)
                for b in new_texts:
                    if b != "":
                        b = ' ' + b
                    res.append(w + b)    
            return res
            
        ans = sorted(dfs(0))
        return ans