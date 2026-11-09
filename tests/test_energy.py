import pytest

from cat_care import Cat, Emotion, play_with_cat


def test_new_cat_starts_with_full_energy():
    cat = Cat("Mochi")

    assert cat.CatEnergy == 100
    assert cat.CatHunger == 50
    assert cat.CatEmotion is Emotion.CONTENT


@pytest.mark.parametrize(
    ("minutes", "expected_energy", "expected_hunger"),
    [
        (1, 99, 51),
        (10, 90, 60),
        (100, 0, 100),
        (150, 0, 100),
    ],
)
def test_play_updates_energy_and_hunger(minutes, expected_energy, expected_hunger):
    cat = Cat("Mochi")

    result = play_with_cat(cat, minutes)

    assert cat.CatEnergy == expected_energy
    assert cat.CatHunger == expected_hunger
    assert result is None


@pytest.mark.parametrize(
    ("minutes", "error"),
    [
        (0, ValueError),
        (-1, ValueError),
        (True, TypeError),
        (False, TypeError),
        (1.5, TypeError),
        ("10", TypeError),
        (None, TypeError),
    ],
)
def test_invalid_play_time_leaves_state_unchanged(minutes, error):
    cat = Cat("Mochi")
    play_with_cat(cat, 10)
    before = (cat.CatEnergy, cat.CatHunger, cat.CatEmotion)

    with pytest.raises(error):
        play_with_cat(cat, minutes)

    assert (cat.CatEnergy, cat.CatHunger, cat.CatEmotion) == before