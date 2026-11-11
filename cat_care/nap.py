from .core import Cat


def nap_cat(cat: Cat, minutes: int) -> int:
    """Restore energy and return the number of points actually restored."""
    if not isinstance(cat, Cat):
        raise TypeError("cat must be a Cat object.")
    if type(minutes) is not int:
        raise TypeError("Nap time must be a whole number of minutes.")
    if minutes <= 0:
        raise ValueError("Nap time must be greater than zero.")

    previous_energy = cat.CatEnergy
    cat._energy = min(100, previous_energy + minutes * 2)
    return cat.CatEnergy - previous_energy