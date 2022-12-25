# 1. Sort when multiple key words, and also simple data structures like dictionary, set... etc.
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        res = []
        id_mp = {}
        for i, sid in enumerate(student_id):
            id_mp[i] = sid
            
        for i, r in enumerate(report):
            score = 0
            words = r.split()
            for word in words:
                if word in positive_feedback:
                    score += 3
                if word in negative_feedback:
                    score -= 1
            res.append((id_mp[i], score))
            
        res.sort(key = lambda x:(-x[1], x[0]))
        ans = []
        for i in range(k):
            ans.append(res[i][0])
        return ans
        