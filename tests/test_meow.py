import pytest 

from cat_care import Cat, meow_cat

def test_meow_once():
    cat=Cat("Mochi")
    assert meow_cat(cat,1)== "Mochi: Meow!"

def test_meow_three_times(): 
    cat = Cat("Mochi")
    assert meow_cat(cat,3) == "Mochi: Meow! Meow! Meow!"

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