from math import inf

import pytest

from cat_care import Cat, Food, feed_cat


def test_buy_adds_only_to_this_inventory_and_coins_are_unlimited():
    cat = Cat("Mochi")
    other = Cat("Luna")
    assert cat.shop.balance == inf
    assert cat.shop.quantity(Food.FISH) == 0

    cat.shop.buy(Food.FISH, 10**12)
    cat.shop.buy(Food.FISH)

    assert cat.shop.quantity(Food.FISH) == 10**12 + 1
    assert cat.shop.balance == inf
    assert cat.shop.total_spent == (10**12 + 1) * 8
    assert other.shop.total_spent == 0
    assert other.shop.quantity(Food.FISH) == 0


@pytest.mark.parametrize(("item", "quantity", "error"), [
    ("fish", 1, TypeError),
    (Food.FISH, True, TypeError),
    (Food.FISH, 1.5, TypeError),
    (Food.FISH, 0, ValueError),
    (Food.FISH, -2, ValueError),
])
def test_invalid_purchase_leaves_inventory_empty(item, quantity, error):
    shop = Cat("Mochi").shop
    with pytest.raises(error):
        shop.buy(item, quantity)
    assert shop.quantity(Food.FISH) == 0
    assert shop.total_spent == 0


def test_batch_feed_needs_the_whole_order():
    cat = Cat("Mochi")
    cat.shop.buy(Food.TREAT)
    cat.shop.buy(Food.FISH)
    with pytest.raises(ValueError, match="shop"):
        feed_cat(cat, [Food.TREAT, Food.FISH, Food.FISH])
    assert cat.CatHunger == 50
    assert cat.shop.quantity(Food.TREAT) == 1
    assert cat.shop.quantity(Food.FISH) == 1

    feed_cat(cat, [Food.TREAT, Food.FISH])
    assert cat.shop.total_spent == 10
    assert cat.shop.quantity(Food.TREAT) == 0
    assert cat.shop.quantity(Food.FISH) == 0
    with pytest.raises(ValueError, match="shop"):
        feed_cat(cat, Food.FISH)


def test_water_requires_stock_and_thirst_stops_at_zero():
    cat = Cat("Mochi")
    with pytest.raises(ValueError, match="water"):
        feed_cat(cat, Food.WATER)
    assert cat.CatThirst == 50
    cat.shop.buy(Food.WATER, 3)
    for expected in (25, 0, 0):
        feed_cat(cat, Food.WATER)
        assert cat.CatThirst == expected
    assert cat.shop.quantity(Food.WATER) == 0
