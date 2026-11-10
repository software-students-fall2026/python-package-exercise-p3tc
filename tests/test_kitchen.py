import pytest

from cat_care import Cat, Food, Kitchen, feed_cat


@pytest.mark.parametrize(
    ("ingredients", "expected_dish"),
    [
        ([Food.FISH, Food.KIBBLE], Food.FISH_KIBBLE_BOWL),
        ([Food.FISH, Food.TREAT], Food.FISH_TREAT_BITES),
        ([Food.KIBBLE, Food.TREAT], Food.KIBBLE_TREAT_MIX),
        ([Food.FISH, Food.KIBBLE, Food.TREAT], Food.CAT_FEAST),
    ],
)
def test_synthesize_matches_recipes_in_either_order(ingredients, expected_dish):
    kitchen = Kitchen()

    assert kitchen.synthesize(ingredients) is expected_dish
    assert kitchen.synthesize(ingredients[::-1]) is expected_dish
    assert kitchen.get_inventory() == {expected_dish: 2}
    assert expected_dish.value == sum(ingredient.value for ingredient in ingredients)


@pytest.mark.parametrize(
    ("ingredients", "error"),
    [
        (Food.FISH, TypeError),
        ([Food.FISH, "kibble"], TypeError),
        ([], ValueError),
        ([Food.FISH], ValueError),
        ([Food.FISH, Food.FISH, Food.KIBBLE], ValueError),
        ([Food.FISH_KIBBLE_BOWL, Food.TREAT], ValueError),
    ],
)
def test_invalid_ingredients_leave_inventory_unchanged(ingredients, error):
    kitchen = Kitchen()
    dish = kitchen.synthesize([Food.FISH, Food.TREAT])

    with pytest.raises(error):
        kitchen.synthesize(ingredients)

    assert kitchen.get_inventory() == {dish: 1}


def test_inventory_is_a_copy_and_belongs_to_one_kitchen():
    kitchen = Kitchen()
    other_kitchen = Kitchen()

    assert kitchen.get_inventory() == {}
    dish = kitchen.synthesize([Food.FISH, Food.TREAT])
    inventory = kitchen.get_inventory()
    inventory[dish] = 99

    assert kitchen.get_inventory() == {dish: 1}
    assert other_kitchen.get_inventory() == {}


def test_feed_consumes_one_serving_at_a_time(capsys):
    kitchen = Kitchen()
    cat = Cat("Mochi")
    dish = kitchen.synthesize([Food.KIBBLE, Food.TREAT])
    kitchen.synthesize([Food.KIBBLE, Food.TREAT])

    kitchen.feed(cat, dish)

    assert cat.CatHunger == 30
    assert kitchen.get_inventory() == {dish: 1}
    assert "Fullness: 70/100" in capsys.readouterr().out

    kitchen.feed(cat, dish)

    assert cat.CatHunger == 10
    assert kitchen.get_inventory() == {}


@pytest.mark.parametrize(
    ("cat", "dish", "error"),
    [
        (None, Food.FISH_TREAT_BITES, TypeError),
        (Cat("Mochi"), "fish treat bites", TypeError),
        (Cat("Mochi"), Food.FISH, ValueError),
        (Cat("Mochi"), Food.CAT_FEAST, ValueError),
    ],
)
def test_invalid_feed_leaves_inventory_and_cat_unchanged(cat, dish, error, capsys):
    kitchen = Kitchen()
    stocked_dish = kitchen.synthesize([Food.FISH, Food.TREAT])

    with pytest.raises(error):
        kitchen.feed(cat, dish)

    assert kitchen.get_inventory() == {stocked_dish: 1}
    if isinstance(cat, Cat):
        assert cat.CatHunger == 50
    assert capsys.readouterr().out == ""


def test_existing_feed_cat_accepts_a_cooked_dish():
    cat = Cat("Mochi")

    feed_cat(cat, Food.FISH_KIBBLE_BOWL)

    assert cat.CatHunger == 5