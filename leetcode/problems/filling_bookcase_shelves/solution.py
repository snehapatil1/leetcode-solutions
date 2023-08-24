class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        no_of_books = len(books)
        dp = [sys.maxsize] * no_of_books
        dp[0] = books[0][1]

        for idx in range(1, no_of_books):
            width, height = books[idx][0], books[idx][1]
            dp[idx] = dp[idx - 1] + height
            for j in range(idx - 1, -1, -1):
                if width + books[j][0] > shelfWidth:
                    break
                width += books[j][0]
                height = max(height, books[j][1])
                dp[idx] = min(dp[idx], (dp[j - 1] + height) if j - 1 >= 0 else height)
        
        return dp[no_of_books - 1]
