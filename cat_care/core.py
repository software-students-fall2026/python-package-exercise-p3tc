from enum import Enum


class Food(Enum):
    FISH = 30
    KIBBLE = 15
    TREAT = 5


class Emotion(Enum):
    HUNGRY = "hungry"
    CONTENT = "content"
    HAPPY = "happy"


_FACES = {
    Emotion.HUNGRY: "T.T",
    Emotion.CONTENT: "o.o",
    Emotion.HAPPY: "^.^",
}


class Cat:
    def __init__(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Cat name must be a string.")
        name = name.strip()
        if not name:
            raise ValueError("Cat name cannot be empty.")

        self.CatName = name
        self._hunger = 50

    @property
    def CatHunger(self) -> int:
        return self._hunger

    @property
    def CatEmotion(self) -> Emotion:
        if self.CatHunger >= 70:
            return Emotion.HUNGRY
        if self.CatHunger <= 30:
            return Emotion.HAPPY
        return Emotion.CONTENT


def create_cat(name: str) -> Cat:
    cat = Cat(name)
    print(draw_cat(cat))
    return cat


def feed_cat(cat: Cat, food: Food | list[Food]) -> None:
    if isinstance(food, Food):
        foods = [food]
    elif isinstance(food, list):
        foods = food
    else:
        raise TypeError("Food must be a Food value or a list of Food values.")

    if not foods:
        raise ValueError("Give the cat at least one food item.")
    if any(not isinstance(item, Food) for item in foods):
        raise TypeError("Every item must be a Food value.")

    hunger_reduction = sum(item.value for item in foods)
    cat._hunger = max(0, cat.CatHunger - hunger_reduction)
    fullness = 100 - cat.CatHunger
    print(f"{cat.CatName} | Fullness: {fullness}/100 | Mood: {cat.CatEmotion.value}")


def play_with_cat(cat: Cat, minutes: int) -> None:
    if type(minutes) is not int:
        raise TypeError("Play time must be a whole number of minutes.")
    if minutes <= 0:
        raise ValueError("Play time must be greater than zero.")

    cat._hunger = min(100, cat.CatHunger + minutes)


def draw_cat(cat: Cat) -> str:
    emotion = cat.CatEmotion
    return "\n".join(
        (
            f"{cat.CatName} [{emotion.value}]",
            " /\\_/\\",
            f"( {_FACES[emotion]} )",
        )
    )