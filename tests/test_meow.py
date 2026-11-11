import pytest 

from cat_care import Cat, Food, meow_cat, play_with_cat, feed_cat

def test_meow_once():
    cat=Cat("Mochi")
    assert meow_cat(cat,1)== "Mochi: Meow."

def test_meow_three_times(): 
    cat = Cat("Mochi")
    assert meow_cat(cat,3) == "Mochi: Meow. Meow. Meow."

def test_meow_rejects_zero():
    cat = Cat("Mochi")
    with pytest.raises(ValueError):
        meow_cat(cat, 0)

def test_meow_rejects_negative_number():
    cat = Cat("Mochi")
    with pytest.raises(ValueError):
        meow_cat(cat, -2)

def test_meow_rejects_string():
    cat = Cat("Mochi")
    with pytest.raises(TypeError):
        meow_cat(cat, "three")

def test_meow_rejects_invalid_cat():
    with pytest.raises(TypeError):
        meow_cat("Mochi", 2)

def test_meow_rejects_boolean():
    cat = Cat("Mochi")
    with pytest.raises(TypeError):
        meow_cat(cat, True)

def test_meow_content(): 
    cat = Cat("Mochi")

    assert cat.CatEmotion.value == "content"
    assert meow_cat(cat,2) == "Mochi: Meow. Meow."

def test_meow_hungry(): 
    cat = Cat("Mochi")
    play_with_cat(cat,25)

    assert cat.CatEmotion.value == "hungry"
    assert meow_cat(cat, 2) == "Mochi: MEOOOW!! MEOOOW!!"

def test_meow_happy(): 
    cat = Cat("Mochi")
    cat.shop.buy(Food.FISH)
    feed_cat(cat, Food.FISH)

    assert cat.CatEmotion.value == "happy"
    assert meow_cat(cat,2) == "Mochi: Meow!♡ Meow!♡"