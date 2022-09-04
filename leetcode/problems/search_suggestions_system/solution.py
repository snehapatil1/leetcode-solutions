class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        output = []
        idx = 0
        search_for = searchWord[idx]
        while idx < len(searchWord):
            matching_words = []
            for word in products:
                if word.startswith(search_for):
                    if len(matching_words) < 3:
                        matching_words.append(word)
            search_for = searchWord[:idx+2]
            idx += 1
            output.append(matching_words)
    
        return output