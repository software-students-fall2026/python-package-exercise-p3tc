from collections import Counter

from .core import Cat, Food, feed_cat


_RECIPES = {
    frozenset((Food.FISH, Food.KIBBLE)): Food.FISH_KIBBLE_BOWL,
    frozenset((Food.FISH, Food.TREAT)): Food.FISH_TREAT_BITES,
    frozenset((Food.KIBBLE, Food.TREAT)): Food.KIBBLE_TREAT_MIX,
    frozenset((Food.FISH, Food.KIBBLE, Food.TREAT)): Food.CAT_FEAST,
}
_COOKED_DISHES = frozenset(_RECIPES.values())

# Track all Synthesized food
class Kitchen:

    def __init__(self) -> None:
        self._inventory: Counter[Food] = Counter()

    # Synthesize food accoridng to RECIPE
    def synthesize(self, ingredients: list[Food]) -> Food:
        if not isinstance(ingredients, list):
            raise TypeError("Ingredients must be a list of Food values.")
        if any(not isinstance(ingredient, Food) for ingredient in ingredients):
            raise TypeError("Every ingredient must be a Food value.")

        recipe = frozenset(ingredients)
        dish = _RECIPES.get(recipe)
        if dish is None or len(recipe) != len(ingredients):
            raise ValueError("Ingredients must match a recipe exactly.")

        self._inventory[dish] += 1
        return dish

    # Just a dict of everything so far
    def get_inventory(self) -> dict[Food, int]:
        """Return a copy of the remaining servings by dish."""
        return dict(self._inventory)

    # Feed by this func deduce the amt reserved in the kitchen
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