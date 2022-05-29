class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
       
        string_list_length = len(strs)
        
        if (string_list_length < 1) or (string_list_length > 100):
            return 0
        
        string_length = len(strs[0]) if (strs and strs[0]) else 0
        
        if (string_length < 1) or (string_length > 1000):
            return 0
        
        delete_columns_count = 0
        
        for col_idx in range(string_length):
            index_str = []
            for row in strs:
                index_str.append(row[col_idx])
            sorted_str = [x for x in index_str]
            sorted_str.sort()
            if index_str != sorted_str:
                delete_columns_count += 1
        
        return delete_columns_count