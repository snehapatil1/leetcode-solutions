# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
import random

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        guessed = 0
        while guessed < 10:
            randomChoice = random.choice(wordlist)
            matches = master.guess(randomChoice)
            if matches == 6:
                print("You guessed the secret word correctly.")
                return
            else:
                wordlist.remove(randomChoice)
                new_list = []
                for word in wordlist:
                    counter = 0
                    for x in range(6):
                        if word[x] == randomChoice[x]:
                            counter += 1
                    if counter == matches:
                        new_list.append(word)
                wordlist = new_list
                
            