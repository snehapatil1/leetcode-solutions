class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        
        res = []
        factor = 2
        
        while factor <= finalSum:
            if not(finalSum):
                break
            after_num = finalSum - factor

            if finalSum == factor:
                val = factor
            elif after_num == factor:
                val = finalSum
            else:
                if factor <= after_num:
                    val = factor
                else:
                    if after_num not in res:
                        val = after_num
                    else:
                        val = finalSum

            res.append(val)

            factor += 2
            finalSum -= val
        
        return res