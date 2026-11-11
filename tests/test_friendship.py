import pytest

from cat_care.core import Cat
from cat_care.cat_manager import CatManager

def test_new_friendship_starts_at_zero():
    manager = CatManager()
    cat_a = Cat("Leo")
    cat_b = Cat("Glenn")

    friendship = manager.get_friendship(cat_a, cat_b)
    assert friendship.score == 0

def test_friendship_same_regardless_of_argument_order():
    manager = CatManager()
    cat_a = Cat("Leo")
    cat_b = Cat("Glenn")

    friendship_1 = manager.get_friendship(cat_a, cat_b)
    friendship_2 = manager.get_friendship(cat_b, cat_a)
    assert friendship_1 is friendship_2

def test_play_together_updates_friendship():
    manager = CatManager()
    cat_a = Cat("Leo")
    cat_b = Cat("Glenn")

    friendship = manager.play_together(cat_a, cat_b, 5)
    assert friendship.score == 5
    assert cat_a.CatHunger == 55
    assert cat_b.CatHunger == 55
    assert cat_a.CatEnergy == 95
    assert cat_b.CatEnergy == 95

def test_repeated_play_accumulates_friendship():
    manager = CatManager()
    cat_a = Cat("Leo")
    cat_b = Cat("Glenn")

    manager.play_together(cat_a, cat_b, 5)
    friendship = manager.play_together(cat_b, cat_a, 3)
    assert friendship.score == 8

def test_play_together_rejects_invalid_cats():
    manager = CatManager()
    cat = Cat("Leo")

    with pytest.raises(TypeError):
        manager.play_together(cat, "Glenn", 5)

def test_play_together_rejects_invalid_minutes():
    manager = CatManager()
    cat_a = Cat("Leo")
    cat_b = Cat("Glenn")

    with pytest.raises(TypeError):
        manager.play_together(cat_a, cat_b, 2.5)

    with pytest.raises(ValueError):
        manager.play_together(cat_a, cat_b, 0)

def test_draw_cats_together_returns_string():
    manager = CatManager()
    cat_a = Cat("Leo")
    cat_b = Cat("Glenn")

    drawing = manager.draw_cats_together(cat_a, cat_b)
    assert isinstance(drawing, str)
    assert "Leo" in drawing
    assert "Glenn" in drawing

def test_draw_cats_together_rejects_invalid_cats():
    manager = CatManager()
    cat = Cat("Leo")

    with pytest.raises(TypeError):
        manager.draw_cats_together(cat, "Glenn")

def test_invalid_play_leaves_cats_and_friendship_unchanged():
    manager= CatManager()
    cat_a = Cat("Leo")
    cat_b = Cat("Glenn")

    friendship = manager.get_friendship(cat_a, cat_b)

    initial_a = (cat_a.CatHunger, cat_a.CatEnergy)
    initial_b = (cat_b.CatHunger, cat_b.CatEnergy)

    with pytest.raises(ValueError):
        manager.play_together( cat_a, cat_b, 0)

    assert (cat_a.CatHunger,  cat_a.CatEnergy) == initial_a
    assert (cat_b.CatHunger, cat_b.CatEnergy) == initial_b
    assert friendship.score == 0
    
def test_different_cat_pairs_have_separate_friendships():
    manager = CatManager()
    cat_a = Cat("Leo")
    cat_b = Cat("Glenn")
    cat_c = Cat("Mochi")

    friendship_1 = manager.get_friendship(cat_a, cat_b)
    friendship_2 = manager.get_friendship(cat_a, cat_c)
    assert friendship_1 is not friendship_2
    assert friendship_1.score == 0
    assert friendship_2.score == 0

def test_friendship_persists_after_lookup():
    manager = CatManager()
    cat_a = Cat("Leo")
    cat_b = Cat("Glenn")

    friendship_1 = manager.get_friendship(cat_a, cat_b)
    friendship_1.score = 10

    friendship_2 = manager.get_friendship(cat_b, cat_a)
    assert friendship_2.score == 10

def test_playing_with_different_cats_keeps_scores_separate():
    manager = CatManager()
    cat_a = Cat("Leo")
    cat_b = Cat("Glenn")
    cat_c = Cat("Milo")

    friendship_1 = manager.play_together(cat_a, cat_b, 5)
    friendship_2 = manager.play_together(cat_a, cat_c, 3)
    assert friendship_1.score == 5
    assert friendship_2.score == 3

def test_play_together_affects_both_cats_equally():
    manager = CatManager()
    cat_a = Cat("Leo")
    cat_b = Cat("Glenn")

    manager.play_together(cat_a, cat_b, 10)
    assert cat_a.CatHunger == cat_b.CatHunger
    assert cat_a.CatEnergy == cat_b.CatEnergy

def test_play_together_accepts_one_minute():
    manager = CatManager()
    cat_a = Cat("Leo")
    cat_b = Cat("Glenn")

    friendship = manager.play_together(cat_a, cat_b, 1)
    assert friendship.score == 1

def test_play_together_rejects_none_cats():
    manager = CatManager()
    cat = Cat("Leo")

    with pytest.raises(TypeError):
        manager.play_together(cat, None, 5)
