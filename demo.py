from cat_care import (
    CatManager,
    Food,
    Kitchen,
    create_cat,
    draw_cat,
    feed_cat,
    meow_cat,
    nap_cat,
    play_with_cat,
)


def main() -> None:
    cat = create_cat("Mochi")

    manager = CatManager()
    manager.add_cat(cat)
    manager.add_cat(create_cat("Luna"))
    print(f"Registered cats ({manager.count_cats()}): {', '.join(manager.list_cats())}")
    cat = manager.get_cat("Mochi")
    print(f"Starting status: {manager.get_cat_status('Mochi')}")

    print("\nMochi says hello!")
    print(meow_cat(cat, 3))

    print("\nWelcome to the cat shop! You have unlimited coins.")
    print(f"Coin balance: {cat.shop.balance}")
    for item, price in cat.shop.prices.items():
        print(f"{item.name.lower()}: {price} coins")
        cat.shop.buy(item)
    print(f"Bought one of each item. Total spent: {cat.shop.total_spent} coins.")

    print("\nMochi plays for 25 minutes.")
    play_with_cat(cat, 25)
    print(draw_cat(cat))

    print(f"Energy before nap: {cat.CatEnergy}/100")
    restored = nap_cat(cat, 5)
    print(f"Mochi restores {restored} energy, now at {cat.CatEnergy}/100.")

    print("\nMochi drinks some water.")
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

    print("\nMochi eats kibble and a treat.")
    feed_cat(cat, [Food.KIBBLE, Food.TREAT])
    print(draw_cat(cat))

    print("\nMochi has some milk.")
    feed_cat(cat, Food.MILK)
    print(f"Final status: {manager.get_cat_status('Mochi')}")

    manager.remove_cat("Luna")
    print(f"Cats after removing Luna ({manager.count_cats()}): {', '.join(manager.list_cats())}")


if __name__ == "__main__":
    main()