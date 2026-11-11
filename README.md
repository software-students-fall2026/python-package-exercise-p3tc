










## API Reference

Import the main API from `cat_care`. The module names below show where each API is defined.

### `cat_manager.py` — Managing cats and friendships

`CatManager()` creates an empty registry of cats and their friendships.

| Method | Description |
| --- | --- |
| `add_cat(cat)` | Registers a `Cat` under its name. A duplicate name raises `ValueError`. |
| `remove_cat(name)` | Removes a registered cat by name. An unknown name raises `ValueError`. |
| `get_cat(name)` | Returns the registered `Cat` with that name. An unknown name raises `ValueError`. |
| `list_cats()` | Returns a list of registered cat names. |
| `count_cats()` | Returns the number of registered cats. |
| `get_cat_status(name)` | Returns a dictionary with the cat's `name`, `hunger`, `energy`, `thirst`, and `emotion`. |
| `get_friendship(cat_a, cat_b)` | Returns the pair's `Friendship`. A new pair starts at `0`. Reversing the argument order returns the same friendship. |
| `play_together(cat_a, cat_b, minutes)` | Plays with both cats and adds one friendship point per minute. Returns the updated `Friendship`. |
| `draw_cats_together(cat_a, cat_b)` | Returns a side-by-side ASCII drawing. The gap narrows as the friendship score increases. |

#### Example

```python
from cat_care import CatManager, create_cat

manager = CatManager()
mochi = create_cat("Mochi")
luna = create_cat("Luna")
manager.add_cat(mochi)
manager.add_cat(luna)

print(manager.list_cats())                    # ['Mochi', 'Luna']
print(manager.count_cats())                   # 2
print(manager.get_cat("Mochi").CatName)        # Mochi
print(manager.get_cat_status("Mochi"))

print(manager.get_friendship(mochi, luna).score)  # 0
friendship = manager.play_together(mochi, luna, 10)
print(friendship.score)                         # 10
print(manager.draw_cats_together(mochi, luna))

manager.remove_cat("Luna")
print(manager.list_cats())                    # ['Mochi']
```

### `core.py` — Cats, food, toys, and daily care

- `Food` defines shop items and cooked dishes. Each member's `.value` is a pair of hunger and thirst points removed. For example, `Food.FISH.value` is `(30, 0)` and `Food.WATER.value` is `(0, 25)`.
- `Emotion` defines the cat's mood based on hunger. `HAPPY` covers `0–30`, `CONTENT` covers `31–69`, and `HUNGRY` covers `70–100`.
- `Toy` provides `Toy.BALL` and `Toy.FEATHER` for `play_with_cat()`.
- `Cat(name)` creates a cat with hunger `50`, energy `100`, and thirst `50`. Read its state through `CatName`, `CatHunger`, `CatEnergy`, `CatThirst`, and `CatEmotion`. Use `cat.shop` to access that cat's shop inventory.

| Function | Description |
| --- | --- |
| `create_cat(name)` | Creates a `Cat`, prints its initial ASCII drawing, and returns the cat. |
| `feed_cat(cat, food)` | Accepts one `Food` or a nonempty list of `Food` values. Consumes any shop items from the cat's inventory, reduces hunger and thirst, and prints the cat's fullness and mood. Use `Kitchen.feed()` when serving a dish from kitchen inventory. |
| `play_with_cat(cat, minutes, toy=None)` | Increases hunger and uses energy. The optional toy changes the rates shown below. |
| `draw_cat(cat)` | Returns an ASCII drawing of the cat with its name and current mood. |
| `meow_cat(cat, times)` | Returns the cat's name followed by its mood-based meow, repeated `times` times. |

| Toy | Hunger added per minute | Energy used per minute |
| --- | ---: | ---: |
| `None` | 1 | 1 |
| `Toy.BALL` | 2 | 2 |
| `Toy.FEATHER` | 1 | 2 |

Hunger stays at or below `100`, and energy stays at or above `0`. Play durations and meow counts must be positive integers.

#### Example

```python
from cat_care import Food, Toy, create_cat, draw_cat, feed_cat, meow_cat, play_with_cat

cat = create_cat("Mochi")
cat.shop.buy(Food.FISH)
cat.shop.buy(Food.WATER)
feed_cat(cat, [Food.FISH, Food.WATER])

play_with_cat(cat, 5, toy=Toy.BALL)
print(cat.CatHunger, cat.CatEnergy, cat.CatThirst)  # 30 90 25
print(draw_cat(cat))
print(meow_cat(cat, 2))
```

### `friendship.py` — Friendship records

`Friendship(cat_a, cat_b)` creates a record with references to both cats and a starting `score` of `0`. Use `CatManager.get_friendship()` to retrieve the record used by the manager during joint play.

#### Example

```python
from cat_care import Cat
from cat_care.friendship import Friendship

friendship = Friendship(Cat("Mochi"), Cat("Luna"))
print(friendship.cat_a.CatName, friendship.cat_b.CatName, friendship.score)
# Mochi Luna 0
```

### `kitchen.py` — Cooking and serving dishes

`Kitchen(shop)` creates an empty kitchen that uses the supplied `Shop` as its ingredient inventory.

| Method | Description |
| --- | --- |
| `synthesize(ingredients)` | Accepts a list of `Food` ingredients, consumes them from the shop inventory, and returns the cooked dish. The ingredients must match a recipe exactly, in any order. |
| `get_inventory()` | Returns a copy of the kitchen's inventory as a dictionary of dishes and remaining servings. |
| `feed(cat, dish)` | Serves one cooked dish to the cat and removes one serving from the kitchen inventory. An out-of-stock dish raises `ValueError`. |

#### Recipes

| Dish | Ingredients |
| --- | --- |
| `Food.FISH_KIBBLE_BOWL` | `FISH`, `KIBBLE` |
| `Food.FISH_TREAT_BITES` | `FISH`, `TREAT` |
| `Food.KIBBLE_TREAT_MIX` | `KIBBLE`, `TREAT` |
| `Food.CAT_FEAST` | `FISH`, `KIBBLE`, `TREAT` |
| `Food.SOFT_KIBBLE` | `KIBBLE`, `WATER` |
| `Food.MILKY_TREATS` | `TREAT`, `MILK` |
| `Food.FISH_SOUP` | `FISH`, `BROTH` |
| `Food.FISH_KIBBLE_STEW` | `FISH`, `KIBBLE`, `BROTH` |

#### Example

```python
from cat_care import Cat, Food, Kitchen

cat = Cat("Mochi")
cat.shop.buy(Food.FISH)
cat.shop.buy(Food.BROTH)

kitchen = Kitchen(cat.shop)
soup = kitchen.synthesize([Food.FISH, Food.BROTH])
print(kitchen.get_inventory().get(soup, 0))  # 1

kitchen.feed(cat, soup)
print(kitchen.get_inventory().get(soup, 0))  # 0
```

### `nap.py` — Restoring energy

`nap_cat(cat, minutes)` restores two energy points per minute, up to `100`. It returns the number of points actually restored. The duration must be a positive integer.

#### Example

```python
from cat_care import Cat, nap_cat, play_with_cat

cat = Cat("Mochi")
play_with_cat(cat, 10)
restored = nap_cat(cat, 3)
print(restored, cat.CatEnergy)  # 6 96
```

### `shop.py` — Buying and tracking supplies

`Shop()` creates an empty shop inventory. Each cat starts with its own `Shop` at `cat.shop`.

| API | Description |
| --- | --- |
| `buy(item, quantity=1)` | Buys the requested number of a catalog item, adds it to inventory, and updates `total_spent`. The quantity must be a positive integer. |
| `quantity(item)` | Returns the number of units of that item currently in stock, or `0` when there is no stock. |
| `prices` | A read-only mapping from shop items to their unit prices. |
| `total_spent` | The total number of coins spent on purchases in this shop. |
| `balance` | Returns `float("inf")` because players have unlimited coins. |

#### Example

```python
from cat_care import Food, Shop

shop = Shop()
shop.buy(Food.FISH, quantity=2)
print(shop.prices[Food.FISH])    # 8
print(shop.quantity(Food.FISH))  # 2
print(shop.total_spent)          # 16
print(shop.balance)              # inf
```

## Run the Demo

See [demo.py](demo.py) for a complete walkthrough. Run it from the project root.

```bash
pipenv run python demo.py
```