from sortedcontainers import SortedSet
import collections

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodRating = defaultdict(int)
        self.foodCuisine = defaultdict(str)
        self.cuisineFoods = defaultdict(SortedSet)
        
        for idx in range(len(foods)):
            self.foodRating[foods[idx]] = ratings[idx]
            self.foodCuisine[foods[idx]] = cuisines[idx]
            self.cuisineFoods[cuisines[idx]].add((-ratings[idx], foods[idx]))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foodCuisine[food]
        self.cuisineFoods[cuisine].remove((-self.foodRating[food], food))
        self.foodRating[food] = newRating
        self.cuisineFoods[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisineFoods[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)