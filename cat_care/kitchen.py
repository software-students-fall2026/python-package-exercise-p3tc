from collections import Counter

from .core import Cat, Food, feed_cat
from .shop import Shop


_RECIPES = {
    frozenset((Food.FISH, Food.KIBBLE)): Food.FISH_KIBBLE_BOWL,
    frozenset((Food.FISH, Food.TREAT)): Food.FISH_TREAT_BITES,
    frozenset((Food.KIBBLE, Food.TREAT)): Food.KIBBLE_TREAT_MIX,
    frozenset((Food.FISH, Food.KIBBLE, Food.TREAT)): Food.CAT_FEAST,
    frozenset((Food.KIBBLE, Food.WATER)): Food.SOFT_KIBBLE,
    frozenset((Food.TREAT, Food.MILK)): Food.MILKY_TREATS,
    frozenset((Food.FISH, Food.BROTH)): Food.FISH_SOUP,
    frozenset((Food.FISH, Food.KIBBLE, Food.BROTH)): Food.FISH_KIBBLE_STEW,
}
_COOKED_DISHES = frozenset(_RECIPES.values())

class Kitchen:

    def __init__(self, shop: Shop) -> None:
        if not isinstance(shop, Shop):
            raise TypeError("Kitchen requires a Shop.")
        self.shop = shop
        self._inventory: Counter[Food] = Counter()
        
    def synthesize(self, ingredients: list[Food]) -> Food:
        if not isinstance(ingredients, list):
            raise TypeError("Ingredients must be a list of Food values.")
        if any(not isinstance(ingredient, Food) for ingredient in ingredients):
            raise TypeError("Every ingredient must be a Food value.")

        recipe = frozenset(ingredients)
        dish = _RECIPES.get(recipe)
        if dish is None or len(recipe) != len(ingredients):
            raise ValueError("Ingredients must match a recipe exactly.")

        self.shop._consume(*ingredients)
        self._inventory[dish] += 1
        return dish

    def get_inventory(self) -> dict[Food, int]:
        return dict(self._inventory)

    def feed(self, cat: Cat, dish: Food) -> None:
        if not isinstance(cat, Cat):
            raise TypeError("cat must be a Cat object.")
        if not isinstance(dish, Food):
            raise TypeError("Dish must be a Food value.")
        if dish not in _COOKED_DISHES:
            raise ValueError("Only cooked dishes can be served from the kitchen.")
        if self._inventory[dish] == 0:
            raise ValueError("This dish is out of stock.")

        feed_cat(cat, dish)
        self._inventory[dish] -= 1
        if self._inventory[dish] == 0:
            del self._inventory[dish]