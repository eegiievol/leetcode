class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
         
        def dfs(v, mat, st, dest):
            if st[v]==1:    #loop
                st[v]=2
                return False            
            if st[v]==2:  #black node
                return True   
            if len(mat[v])==0:  #leaf
                st[v]=2
                return v==dest          
            
            
            st[v]=1 #start processing           
            for nei in mat[v]:
                if not dfs(nei, mat, st, dest):
                    return False
            st[v] = 2 #finished processing          
            return True
        
        if not edges:
            if source!=destination:
                return False
            else:
                return True
        
        mat = defaultdict(list)
        st={} #0-white, 1-gray, 2-black
        for s,d in edges:
            mat[s].append(d)
            st[s]=0 
            st[d]=0         
        
        #print(mat)
        return dfs(source,mat,st,destination)
        
        
        
        
        
