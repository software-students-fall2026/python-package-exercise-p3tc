from cat_care import Food, Kitchen, create_cat, draw_cat, feed_cat, play_with_cat, meow_cat


def main() -> None:
    cat = create_cat("Mochi")

    print("\nMochi says hello!")
    print(meow_cat(cat,3))

    print("\nWelcome to the cat shop! You have unlimited coins.")
    for item, price in cat.shop.prices.items():
        print(f"{item.name.lower()}: {price} coins")
        cat.shop.buy(item)
    print(f"Bought one of each item for Mochi. Total spent: {cat.shop.total_spent} coins.")

    print("\nMochi plays for 25 minutes.")
    play_with_cat(cat, 25)
    print(draw_cat(cat))

    feed_cat(cat, Food.WATER)
    print(f"Mochi drinks some water. Thirst: {cat.CatThirst}/100")

    print("\nThe fish and broth from the shop make one serving of fish soup.")
    kitchen = Kitchen(cat.shop)
    soup = kitchen.synthesize([Food.FISH, Food.BROTH])
    kitchen.feed(cat, soup)
    print(f"Fish left: {cat.shop.quantity(Food.FISH)}")
    print(draw_cat(cat))

    print("\nMochi eats kibble and a treat.")
    feed_cat(cat, [Food.KIBBLE, Food.TREAT])
    print(draw_cat(cat))

    print("\nMochi has some milk.")
    feed_cat(cat, Food.MILK)
    print(f"Thirst: {cat.CatThirst}/100")


if __name__ == "__main__":
    main()
