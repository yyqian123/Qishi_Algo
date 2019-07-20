#Leetcode 207. Course Schedule
from collections import deque
class Solution:
   
    def canFinish(self, numCourses, prerequisites):
        # Write your code here
        edges = {i: [] for i in range(numCourses)}
        degrees = [0 for i in range(numCourses)] 
        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1
            
        queue, count = deque([]), 0
        
        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            count += 1

            for x in edges[node]:
                degrees[x] -= 1
                if degrees[x] == 0:
                    queue.append(x)

        return count == numCourses

      

#Leetcode 399. Evaluate Division
class Solution:
  
    def calcEquation(self, equations, values, queries):

        uf = UnionFind()
        for i in range(len(values)):
            a, b, a_b = equations[i][0], equations[i][1], values[i]
            uf.union(a, b, a_b)
        
        ans = []
        for u, v in queries:
            if u in uf.root and v in uf.root:
                u_ur, root_u = uf.find(u)
                v_vr, root_v = uf.find(v)
     
                if root_u != root_v:
                    ans.append(-1.0)
                else:
                    ans.append(u_ur / v_vr)
            else:
                ans.append(-1.0)
        return ans



#Lintcode 1029. Cheapest Flights within K Stops
class Solution:

    def findCheapestPrice(self, n, flights, src, dst, K):
        distance = [sys.maxsize for i in range(n)]
        distance[src] = 0
        
        for i in range(0, K + 1):
            dN = list(distance)    	
            for u,v,c in flights:
                dN[v]= min(dN[v], distance[u] + c)
            distance = dN
            
        if distance[dst] != sys.maxsize:
            return distance[dst]
        else:
            return -1

          
          
#Lintcode 783. Minimize Risk Path
class Solution:

    def __init__(self):
        self.v = [[] for x in range(0, 1010)]
        self.w = [[] for x in range(0, 1010)]
        self.vis = [0 for _ in range(0, 1010)]
        self.res = 1000000000
    
    def addedge(self, x, y, z):
        self.v[x].append(y)
        self.w[x].append(z)
        
    def helper(self, x, value, n):
        if x == n:
            return value
        if value >= self.res:
            return 1000000000
        self.vis[x] = 1
        temp = 1000000000
        for i in range(0, len(self.v[x])):
            if self.vis[self.v[x][i]] == 1:
                continue
            temp = min(temp, self.helper(self.v[x][i], max(value, self.w[x][i]), n))
            self.res = min(temp, self.res)
        self.vis[x] = 0
        return temp
    
    def getMinRiskValue(self, n, m, x, y, w):
        # Write your code here
        for i in range(0, m):
            self.addedge(x[i], y[i], w[i])
            self.addedge(y[i], x[i], w[i])
        return self.helper(0, 0, n)
