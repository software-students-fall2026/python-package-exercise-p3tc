from cat_care.core import Cat, play_with_cat, feed_cat, Food
from cat_care.cat_manager import CatManager
from cat_care.nap import nap_cat

def test_manager_status_after_playing():
    manager=CatManager()
    cat= Cat("Leo")

    manager.add_cat(cat)
    play_with_cat(cat, 20)

    status = manager.get_cat_status("Leo")

    assert status["hunger"]==70
    assert status["energy"]==80
    assert status["emotion"]=="hungry"
    assert manager.count_cats()==1

def test_manager_status_after_feeding():
    manager=CatManager()
    cat = Cat("Leo")

    manager.add_cat(cat)
    cat.shop.buy(Food.FISH)
    feed_cat(cat, Food.FISH)

    status = manager.get_cat_status("Leo")

    assert status["hunger"]==20
    assert status["emotion"]=="happy"
    assert status["name"]=="Leo"
    assert manager.count_cats()==1

def test_manager_status_after_napping():
    manager=CatManager()
    cat = Cat("Leo")

    manager.add_cat(cat)
    play_with_cat(cat, 30)
    nap_cat(cat, 10)

    status = manager.get_cat_status("Leo")

    assert status["hunger"]==80
    assert status["energy"]==90
    assert status["emotion"]=="hungry"
    assert manager.get_cat("Leo")==cat

def test_manager_keeps_two_cats_separate():
    manager=CatManager()

    leo=Cat("Leo")
    luna=Cat("Luna")

    manager.add_cat(leo)
    manager.add_cat(luna)

    play_with_cat(leo, 20)

    leo_status = manager.get_cat_status("Leo")
    luna_status = manager.get_cat_status("Luna")

    assert leo_status["hunger"]==70
    assert leo_status["energy"]==80
    assert luna_status["hunger"]==50
    assert luna_status["energy"]==100
    assert manager.count_cats()==2