class Solution:
    def checkRecord(self, s: str) -> bool:
        sList = list(s)

        if sList.count('A') >= 2:
            return False
        
        consecutive_L_count = 0

        for ele in sList:
            if ele != 'L' and consecutive_L_count:
                consecutive_L_count = 0
            if ele == 'L':
                consecutive_L_count += 1
                if consecutive_L_count >= 3:
                    return False
        
        if consecutive_L_count >= 3:
            return False
        
        return True
            