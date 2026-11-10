from .core import Cat

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