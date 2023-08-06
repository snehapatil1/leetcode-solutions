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