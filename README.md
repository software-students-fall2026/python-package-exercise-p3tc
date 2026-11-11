# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

## Playing with toys

`play_with_cat(cat, minutes, toy=None)` plays with an existing cat.
It updates the cat's hunger and energy and returns `None`.

| Toy | Hunger added per minute | Energy used per minute |
| --- | --- | --- |
| `None` | 1 | 1 |
| `Toy.BALL` | 2 | 2 |
| `Toy.FEATHER` | 1 | 2 |

Hunger cannot exceed 100, and energy cannot fall below 0.

## Napping

`nap_cat(cat, minutes)` restores 2 energy points per minute, up to 100.
It returns the number of energy points actually restored.

Both functions require a positive integer for `minutes`; booleans are not accepted.
Invalid minute types or toy values raise `TypeError`.
Zero or negative minutes raise `ValueError`.

### Example

```python
from cat_care import Cat, Toy, nap_cat, play_with_cat

cat = Cat("Mochi")
play_with_cat(cat, 10, toy=Toy.BALL)
print(cat.CatHunger, cat.CatEnergy)  # 70 80

restored = nap_cat(cat, 5)
print(restored, cat.CatEnergy)  # 10 90
```

See [demo.py](demo.py) for the runnable example program.
From the project root, run:

```bash
pipenv run python demo.py
```
