from typing import List
from collections import defaultdict

class GraphLeetCode:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """ leetcode #207 """

        prereq = defaultdict(list)
        for c, p in prerequisites:
            prereq[c].append(p)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        def canTake(course):
            if states[course] == VISITED:
                return True
            elif states[course] == VISITING:
                return False
            else:
                states[course] = VISITING
                for r in prereq[course]:
                    if not canTake(r):
                        return False
                states[course] = VISITED
                return True

        for c in range(numCourses):
            if not canTake(c):
                return False
        return True
