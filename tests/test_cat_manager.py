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

def test_add_two_cats():
    manager= CatManager()
    cat1=Cat("Leo")
    cat2=Cat("Luna")

    manager.add_cat(cat1)

    manager.add_cat(cat2)

    assert manager.count_cats()==2

    assert manager.get_cat("Leo")==cat1
    assert manager.get_cat("Luna")==cat2
    assert manager.list_cats()==["Leo", "Luna"]

def test_add_three_cats():
    manager= CatManager()

    cat1=Cat("Leo")
    cat2=Cat("Luna")
    cat3=Cat("Klixy")

    manager.add_cat(cat1)
    manager.add_cat(cat2)
    manager.add_cat(cat3)
    
    assert manager.count_cats()==3
    assert "Leo" in manager.list_cats()
    assert "Luna" in manager.list_cats()
    assert "Klixy" in manager.list_cats()

def test_remove_missing_cat():
    manager=CatManager()
    with pytest.raises(ValueError):
        manager.remove_cat("Unknown")

    assert manager.count_cats()==0
    assert manager.list_cats()==[]

def test_remove_one_of_two_cats():
    manager=CatManager()

    manager.add_cat(Cat("Leo"))
    manager.add_cat(Cat("Luna"))

    manager.remove_cat("Leo")

    assert manager.count_cats()==1
    assert manager.list_cats()==["Luna"]
    assert manager.get_cat("Luna").CatName=="Luna"

def test_get_removed_cat():
    manager=CatManager()

    manager.add_cat(Cat("Leo"))
    manager.remove_cat("Leo")

    with pytest.raises(ValueError):
        manager.get_cat("Leo")

    assert manager.count_cats()==0

def test_add_string_instead_of_cat():
    manager=CatManager()

    with pytest.raises(TypeError):
        manager.add_cat("Leo")

    assert manager.count_cats()==0
    assert manager.list_cats()==[]

def test_add_number_instead_of_cat():
    manager=CatManager()

    with pytest.raises(TypeError):
        manager.add_cat(123)

    assert manager.count_cats()==0
    assert manager.list_cats()==[]

def test_add_none_instead_of_cat():
    manager= CatManager()

    with pytest.raises(TypeError):
        manager.add_cat(None)

    assert manager.count_cats()==0
    assert manager.list_cats()==[]

def test_duplicate_cat_does_not_change_list():
    manager= CatManager()
    manager.add_cat(Cat("Leo"))

    with pytest.raises(ValueError):
        manager.add_cat(Cat("Leo"))

    assert manager.count_cats()==1
    assert manager.list_cats()==["Leo"] 

def test_two_separate_managers():
    manager1= CatManager()
    manager2= CatManager()

    manager1.add_cat(Cat("Leo"))
    manager2.add_cat(Cat("Luna"))

    assert manager1.count_cats()==1
    assert manager2.count_cats()==1
    assert manager1.list_cats()==["Leo"] 
    assert manager2.list_cats()==["Luna"] 

def test_remove_all_cats():
    manager= CatManager()

    manager.add_cat(Cat("Leo"))
    manager.add_cat(Cat("Luna"))

    manager.remove_cat("Leo")
    manager.remove_cat("Luna")

    assert manager.count_cats()== 0
    assert manager.list_cats()==[] 

def test_empty_cat_manager():
    manager= CatManager()

    assert manager.count_cats()== 0
    assert manager.list_cats()==[] 

    with pytest.raises(ValueError):
        manager.get_cat("Leo")

def test_cat_status_emotion():
    manager=CatManager()
    manager.add_cat(Cat("Leo"))

    status = manager.get_cat_status("Leo")

    assert status["name"] == "Leo"
    assert status["emotion"] == "content"
    assert status["hunger"] == 50
    assert status["energy"] == 100
    assert status["thirst"] == 50

def test_status_missing_cat():
    manager=CatManager()

    with pytest.raises(ValueError):
        manager.get_cat_status("Unknown")

    assert manager.count_cats()==0
    assert manager.list_cats()==[]

