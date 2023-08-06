"""
    Question:
        You have information about n different recipes. 
        You are given a string array recipes and a 2D string array ingredients. 
        The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. 
        Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.
        You are also given a string array supplies containing all the ingredients that you initially have, 
        and you have an infinite supply of all of them.
        Return a list of all the recipes that you can create. You may return the answer in any order.
        Note that two recipes may contain each other in their ingredients.
"""

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = set(supplies)

        ans = []
        ingredients_used_in_recipe = defaultdict(set)
        ingredients_unavailable_count = Counter()

        for recipe, ingredient in zip(recipes, ingredients):
            not_available = 0
            for ing in ingredient:
                if ing not in available:
                    not_available += 1
                    ingredients_used_in_recipe[ing].add(recipe)
            if not_available == 0:
                ans.append(recipe)
            else:
                ingredients_unavailable_count[recipe] = not_available
        
        for rcp in ans:
            for recipe in ingredients_used_in_recipe.pop(rcp, set()):
                ingredients_unavailable_count[recipe] -= 1
                if ingredients_unavailable_count[recipe] == 0:
                    ans.append(recipe)
        
        return ans
