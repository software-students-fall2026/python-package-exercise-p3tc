import pytest

from cat_care import Cat, Emotion, Food, create_cat, draw_cat, feed_cat, play_with_cat


def test_create_cat_draws_and_returns_cat(capsys):
    cat = create_cat("  Mochi  ")

    assert isinstance(cat, Cat)
    assert cat.CatName == "Mochi"
    assert cat.CatHunger == 50
    assert cat.CatEmotion is Emotion.CONTENT
    assert capsys.readouterr().out == draw_cat(cat) + "\n"


@pytest.mark.parametrize(
    ("name", "error"),
    [("", ValueError), ("   ", ValueError), (123, TypeError)],
)
def test_create_cat_rejects_invalid_names(name, error):
    with pytest.raises(error):
        create_cat(name)


def test_feed_single_food(capsys):
    cat = Cat("Mochi")

    feed_cat(cat, Food.FISH)

    assert cat.CatHunger == 20
    assert cat.CatEmotion is Emotion.HAPPY
    assert capsys.readouterr().out == "Mochi | Fullness: 80/100 | Mood: happy\n"


def test_feed_list_applies_all_food_and_reports_once(capsys):
    cat = Cat("Mochi")

    feed_cat(cat, [Food.KIBBLE, Food.TREAT])

    assert cat.CatHunger == 30
    assert capsys.readouterr().out.splitlines() == [
        "Mochi | Fullness: 70/100 | Mood: happy"
    ]


def test_feed_caps_fullness_at_100(capsys):
    cat = Cat("Mochi")

    feed_cat(cat, [Food.FISH, Food.FISH])

    assert cat.CatHunger == 0
    assert "Fullness: 100/100" in capsys.readouterr().out


@pytest.mark.parametrize(
    ("food", "error"),
    [([], ValueError), ("fish", TypeError), ([Food.FISH, "fish"], TypeError)],
)
def test_invalid_food_leaves_cat_unchanged(food, error, capsys):
    cat = Cat("Mochi")

    with pytest.raises(error):
        feed_cat(cat, food)

    assert cat.CatHunger == 50
    assert capsys.readouterr().out == ""


def test_play_increases_hunger_and_caps_it():
    cat = Cat("Mochi")

    play_with_cat(cat, 10)

    assert cat.CatHunger == 60
    assert cat.CatEmotion is Emotion.CONTENT

    play_with_cat(cat, 100)

    assert cat.CatHunger == 100
    assert cat.CatEmotion is Emotion.HUNGRY


@pytest.mark.parametrize(
    ("minutes", "error"),
    [(0, ValueError), (-1, ValueError), (1.5, TypeError), (True, TypeError)],
)
def test_invalid_play_time_leaves_cat_unchanged(minutes, error):
    cat = Cat("Mochi")

    with pytest.raises(error):
        play_with_cat(cat, minutes)

    assert cat.CatHunger == 50


@pytest.mark.parametrize(
    ("minutes", "hunger", "emotion", "face"),
    [
        (10, 30, Emotion.HAPPY, "^.^"),
        (11, 31, Emotion.CONTENT, "o.o"),
        (49, 69, Emotion.CONTENT, "o.o"),
        (50, 70, Emotion.HUNGRY, "T.T"),
    ],
)
def test_draw_cat_at_mood_boundaries(minutes, hunger, emotion, face):
    cat = Cat("Mochi")
    feed_cat(cat, Food.FISH)
    play_with_cat(cat, minutes)

    drawing = draw_cat(cat).splitlines()

    assert cat.CatHunger == hunger
    assert cat.CatEmotion is emotion
    assert drawing == [f"Mochi [{emotion.value}]", " /\\_/\\", f"( {face} )"]