class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        weak_characters = 0
        
        properties.sort(key=lambda x:(-x[0],x[1]))
            
        max_attack = properties[0][0]
        max_defense = properties[0][1]
        
        for character in properties:
            if character[0]<max_attack and character[1]<max_defense:
                weak_characters += 1
            else:
                max_attack = character[0]
                max_defense = character[1]
        
        return weak_characters