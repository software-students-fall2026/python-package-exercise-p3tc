from cat_care import Food, create_cat, draw_cat, feed_cat, play_with_cat


def main() -> None:
    cat = create_cat("Mochi")

    print("\nMochi plays for 25 minutes.")
    play_with_cat(cat, 25)
    print(draw_cat(cat))

    print("\nMochi eats a fish.")
    feed_cat(cat, Food.FISH)
    print(draw_cat(cat))

    print("\nMochi eats kibble and a treat.")
    feed_cat(cat, [Food.KIBBLE, Food.TREAT])
    print(draw_cat(cat))


if __name__ == "__main__":
    main()