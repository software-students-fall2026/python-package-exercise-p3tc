import pytest

from cat_care.core import Cat
from cat_care.cat_manager import CatManager

def test_add_cat():
    manager= CatManager()
    cat= Cat("Leo")

    manager.add_cat(cat)

    assert manager.count_cats()==1
    assert manager.get_cat("Leo")==cat
    assert manager.list_cats()==["Leo"]

def test_remove_cat():
    manager=CatManager()
    manager.add_cat(Cat("Leo"))
    manager.remove_cat("Leo")

    assert manager.count_cats()==0
    assert manager.list_cats()==[]

def test_cat_status():
    manager=CatManager()
    manager.add_cat(Cat("Leo"))

    status=manager.get_cat_status("Leo")

    assert status["name"]=="Leo"
    assert status["hunger"]==50
    assert status["energy"]==100
    assert status["thirst"]==50

def test_duplicate_cat():
    manager=CatManager()
    manager.add_cat(Cat("Leo"))

    with pytest.raises(ValueError):
        manager.add_cat(Cat("Leo"))

def test_missing_cat():
    manager=CatManager()

    with pytest.raises(ValueError):
        manager.get_cat("Unknown")
