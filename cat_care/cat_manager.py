from .core import Cat, play_with_cat, draw_cat
from .friendship import Friendship

class CatManager:

    def __init__(self):
        self.cats={}

    def add_cat(self,cat):
        if not isinstance(cat,Cat):
            raise TypeError("Must be a Cat")
        if cat.CatName in self.cats:
            raise ValueError("This cat already exists")
        
        self.cats[cat.CatName]=cat

    def remove_cat(self, name):
        if name not in self.cats:
            raise ValueError("Cat not found")
        
        del self.cats[name]

    def get_cat(self,name):
        if name not in self.cats:
            raise ValueError("Cat not found")
        
        return self.cats[name]
    
    def list_cats(self):
        names=[]
        for name in self.cats:
            names.append(name)

        return names
    
    def count_cats(self):

        return len (self.cats)
    
    def get_cat_status(self,name):
        cat=self.get_cat(name)
        
        return{
            "name": cat.CatName,
            "hunger": cat.CatHunger,
            "energy": cat.CatEnergy,
            "thirst": cat.CatThirst,
            "emotion": cat.CatEmotion.value
        }

    def __init__(self):
        self.cats = {}
        self.friendships={}

    def get_friendship(self, cat_a: Cat, cat_b: Cat) -> Friendship:
        if not isinstance(cat_a, Cat) or not isinstance(cat_b, Cat):
            raise TypeError("Both arguments must be Cat objects.")

        pair = frozenset((cat_a.CatName, cat_b.CatName))

        if pair not in self.friendships:
            self.friendships[pair] = Friendship(cat_a, cat_b)

        return self.friendships[pair]

    def play_together(self, cat_a: Cat, cat_b: Cat, minutes: int) -> Friendship:
        if not isinstance(cat_a, Cat) or not isinstance(cat_b, Cat):
            raise TypeError("Both arguments must be Cat objects.")

        if type(minutes) is not int:
            raise TypeError("Minutes must be a whole number.")

        if minutes <= 0:
            raise ValueError("Minutes must be greater than zero.")

        play_with_cat(cat_a, minutes)
        play_with_cat(cat_b, minutes)

        friendship = self.get_friendship(cat_a, cat_b)
        friendship.score += minutes

        return friendship

    def draw_cats_together(self, cat_a: Cat, cat_b: Cat) -> str:
        if not isinstance(cat_a, Cat) or not isinstance(cat_b, Cat):
            raise TypeError("Both arguments must be Cat objects.")

        friendship = self.get_friendship(cat_a, cat_b)

        drawing_a = draw_cat(cat_a).splitlines()
        drawing_b = draw_cat(cat_b).splitlines()

        if friendship.score == 0:
            spacing = "       "
        elif friendship.score < 10:
            spacing = "   "
        else:
            spacing = " "

        return "\n".join(
            left + spacing + right
            for left, right in zip(drawing_a, drawing_b)
        )
