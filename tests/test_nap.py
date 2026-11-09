import pytest

from cat_care import Cat, nap_cat, play_with_cat


def test_nap_restores_two_energy_per_minute():
    cat = Cat("Mochi")
    play_with_cat(cat, 10)
    hunger_before = cat.CatHunger
    emotion_before = cat.CatEmotion

    restored = nap_cat(cat, 3)

    assert restored == 6
    assert type(restored) is int
    assert cat.CatEnergy == 96
    assert cat.CatHunger == hunger_before
    assert cat.CatEmotion is emotion_before


@pytest.mark.parametrize(
    ("play_minutes", "nap_minutes", "expected_restored"),
    [
        (10, 5, 10),
        (1, 1, 1),
        (100, 1000, 100),
    ],
)
def test_nap_caps_energy_at_100(play_minutes, nap_minutes, expected_restored):
    cat = Cat("Mochi")
    play_with_cat(cat, play_minutes)
    hunger_before = cat.CatHunger

    restored = nap_cat(cat, nap_minutes)

    assert cat.CatEnergy == 100
    assert restored == expected_restored
    assert cat.CatHunger == hunger_before


def test_nap_at_full_energy_returns_zero():
    cat = Cat("Mochi")

    restored = nap_cat(cat, 5)

    assert restored == 0
    assert cat.CatEnergy == 100
    assert cat.CatHunger == 50


@pytest.mark.parametrize(
    ("minutes", "error"),
    [
        (0, ValueError),
        (-1, ValueError),
        (True, TypeError),
        (False, TypeError),
        (1.5, TypeError),
        ("3", TypeError),
        (None, TypeError),
    ],
)
def test_invalid_nap_time_leaves_state_unchanged(minutes, error):
    cat = Cat("Mochi")
    play_with_cat(cat, 10)
    before = (cat.CatEnergy, cat.CatHunger, cat.CatEmotion)

    with pytest.raises(error):
        nap_cat(cat, minutes)

    assert (cat.CatEnergy, cat.CatHunger, cat.CatEmotion) == before


@pytest.mark.parametrize("invalid_cat", [None, "Mochi", {}])
def test_nap_rejects_invalid_cat(invalid_cat):
    with pytest.raises(TypeError):
        nap_cat(invalid_cat, 5)