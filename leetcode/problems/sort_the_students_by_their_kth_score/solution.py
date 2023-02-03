class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        hashMap = {}
        output = []
        for idx, student in enumerate(score):
            hashMap.update({ student[k] : idx })
        
        keys = list(hashMap.keys())
        keys.sort(reverse=True)

        for ele in keys:
            output.append(score[hashMap[ele]])

        return output