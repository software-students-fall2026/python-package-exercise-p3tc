from collections import Counter
from math import inf
from types import MappingProxyType

from .core import Food


class Shop:

    prices = MappingProxyType({
        Food.FISH: 8,
        Food.KIBBLE: 4,
        Food.TREAT: 2,
        Food.WATER: 1,
        Food.MILK: 3,
        Food.BROTH: 4,
    })

    def __init__(self) -> None:
        self.total_spent = 0
        self._inventory: Counter[Food] = Counter()

    @property
    def balance(self) -> float:
        return inf

    def buy(self, item: Food, quantity: int = 1) -> None:
        if not isinstance(item, Food):
            raise TypeError("Choose an item from the shop catalog.")
        if type(quantity) is not int:
            raise TypeError("Quantity must be a whole number.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if item not in self.prices:
            raise ValueError("This item is not sold in the shop.")
        self.total_spent += self.prices[item] * quantity
        self._inventory[item] += quantity

    def quantity(self, item: Food) -> int:
        return self._inventory[item]

    def _require(self, item: Food, quantity: int = 1) -> None:
        if self.quantity(item) < quantity:
            raise ValueError(f"Buy more {item.name.lower()} at the shop first.")

    def _consume(self, *items: Food) -> None:
        needed = Counter(items)
        for item, quantity in needed.items():
            self._require(item, quantity)
        self._inventory.subtract(needed)
