# Topological Sort, O(|V| + |E|). Deal with nodes one by one, if indegree == 0, push into queue, else every out's indegree decrease by 1.
class GNode(object):
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        graph = defaultdict(GNode)
        totalDeps = 0
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegrees += 1
            totalDeps += 1
        q = deque()
        for index, node in graph.items():
            if node.inDegrees == 0:
                q.append(index)
        removed = 0
        while q:
            course = q.pop()
            for nextCourse in graph[course].outNodes:
                graph[nextCourse].inDegrees -= 1
                removed += 1
                
                if graph[nextCourse].inDegrees == 0:
                    q.append(nextCourse)
        if removed == totalDeps:
            return True
        return False
        