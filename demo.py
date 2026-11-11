from cat_care import (
    CatManager,
    Food,
    Kitchen,
    Toy,
    create_cat,
    draw_cat,
    feed_cat,
    meow_cat,
    nap_cat,
    play_with_cat,
)


def main() -> None:
    cat = create_cat("Moon")

    manager = CatManager()
    manager.add_cat(cat)
    manager.add_cat(create_cat("Luna"))
    print(f"Registered cats ({manager.count_cats()}): {', '.join(manager.list_cats())}")
    cat = manager.get_cat("Moon")
    print(f"Starting status: {manager.get_cat_status('Moon')}")

    print("\nMoon says hello!")
    print(meow_cat(cat, 3))

    print("\nWelcome to the cat shop! You have unlimited coins.")
    print(f"Coin balance: {cat.shop.balance}")
    for item, price in cat.shop.prices.items():
        print(f"{item.name.lower()}: {price} coins")
        cat.shop.buy(item)
    print(f"Bought one of each item. Total spent: {cat.shop.total_spent} coins.")

    print("\nMoon plays for 25 minutes.")
    play_with_cat(cat, 25)
    print(draw_cat(cat))
    print(meow_cat(cat, 2))

    print("\nMoon plays with a ball for 2 minutes.")
    play_with_cat(cat, 2, toy=Toy.BALL)
    print(f"Hunger: {cat.CatHunger}/100 | Energy: {cat.CatEnergy}/100")

    print("\nMoon plays with a feather for 2 minutes.")
    play_with_cat(cat, 2, toy=Toy.FEATHER)
    print(f"Hunger: {cat.CatHunger}/100 | Energy: {cat.CatEnergy}/100")

    print(f"\nEnergy before nap: {cat.CatEnergy}/100")
    restored = nap_cat(cat, 5)
    print(f"Moon restores {restored} energy, now at {cat.CatEnergy}/100.")

    print("\nMoon drinks some water.")
    feed_cat(cat, Food.WATER)
    print(f"Thirst: {cat.CatThirst}/100")

    print("\nThe fish and broth make one serving of fish soup.")
    kitchen = Kitchen(cat.shop)
    soup = kitchen.synthesize([Food.FISH, Food.BROTH])
    print(f"Soup servings ready: {kitchen.get_inventory().get(soup, 0)}")
    print(f"Fish left in the shop: {cat.shop.quantity(Food.FISH)}")
    kitchen.feed(cat, soup)
    print(f"Soup servings left: {kitchen.get_inventory().get(soup, 0)}")
    print(draw_cat(cat))

    print("\nMoon eats kibble and a treat.")
    feed_cat(cat, [Food.KIBBLE, Food.TREAT])
    print(draw_cat(cat))
    print(meow_cat(cat, 2))

    print("\nMoon has some milk.")
    feed_cat(cat, Food.MILK)

    luna = manager.get_cat("Luna")
    friendship = manager.get_friendship(cat, luna)
    print(f"\nStarting friendship score: {friendship.score}")
    print(manager.draw_cats_together(cat, luna))

    print("\nMoon and Luna play together for 10 minutes.")
    friendship = manager.play_together(cat, luna, 10)
    print(f"Friendship score after playing: {friendship.score}")
    print(manager.draw_cats_together(cat, luna))

    print(f"\nFinal status: {manager.get_cat_status('Moon')}")
    manager.remove_cat("Luna")
    print(f"Cats after removing Luna ({manager.count_cats()}): {', '.join(manager.list_cats())}")


if __name__ == "__main__":
    main()