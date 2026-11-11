import pytest

from cat_care import Cat, Food, Toy, play_with_cat


@pytest.mark.parametrize(
    ("toy", "expected_hunger", "expected_energy"),
    [
        (None, 60, 90),
        (Toy.BALL, 70, 80),
        (Toy.FEATHER, 60, 80),
    ],
)
def test_play_with_optional_toy(toy, expected_hunger, expected_energy):
    cat = Cat("Mochi")
    thirst_before = cat.CatThirst

    result = play_with_cat(cat, 10, toy=toy)

    assert cat.CatHunger == expected_hunger
    assert cat.CatEnergy == expected_energy
    assert cat.CatThirst == thirst_before
    assert result is None


@pytest.mark.parametrize("toy", [Toy.BALL, Toy.FEATHER])
def test_toy_play_respects_state_limits(toy):
    cat = Cat("Mochi")

    play_with_cat(cat, 100, toy=toy)

    assert cat.CatHunger == 100
    assert cat.CatEnergy == 0


@pytest.mark.parametrize("toy", ["ball", 1, True, [], Food.FISH])
def test_invalid_toy_leaves_state_unchanged(toy):
    cat = Cat("Mochi")
    before = (cat.CatHunger, cat.CatEnergy, cat.CatThirst)

    with pytest.raises(TypeError):
        play_with_cat(cat, 10, toy=toy)

    assert (cat.CatHunger, cat.CatEnergy, cat.CatThirst) == before


@pytest.mark.parametrize(
    ("minutes", "error"),
    [
        (0, ValueError),
        (-1, ValueError),
        (True, TypeError),
        (1.5, TypeError),
    ],
)
def test_invalid_minutes_with_toy_leave_state_unchanged(minutes, error):
    cat = Cat("Mochi")
    before = (cat.CatHunger, cat.CatEnergy, cat.CatThirst)

    with pytest.raises(error):
        play_with_cat(cat, minutes, toy=Toy.BALL)

    assert (cat.CatHunger, cat.CatEnergy, cat.CatThirst) == before