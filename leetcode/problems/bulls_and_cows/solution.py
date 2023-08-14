class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretCount = collections.Counter(secret)
        bulls, cows = 0, 0

        for idx in range(len(guess)):
            if guess[idx] not in secretCount:
                continue
            
            if guess[idx] == secret[idx]:
                bulls += 1
                cows -= int(secretCount[guess[idx]] <= 0)
            elif guess[idx] in secret[:idx]+secret[idx+1:] and secretCount[guess[idx]] > 0:
                cows += int(secretCount[guess[idx]] > 0)
            
            secretCount[guess[idx]] -= 1
        
        return f'{bulls}A{cows}B'