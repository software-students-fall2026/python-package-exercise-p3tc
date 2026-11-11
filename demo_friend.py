from cat_care import CatManager, create_cat

def main() -> None:
    manager = CatManager()
    leo = create_cat("Leo")
    glenn = create_cat("Glenn")

    manager.add_cat(leo)
    manager.add_cat(glenn)
    
    friendship = manager.get_friendship(leo, glenn)
    print(f"Starting friendship: {friendship.score}")
    print(manager.draw_cats_together(leo, glenn))

    print("\nLeo and Glenn play together!")
    friendship = manager.play_together(leo, glenn, 5)
    print(manager.draw_cats_together(leo, glenn))
    print(f"Friendship after playing: {friendship.score}")

    print("\nThe cats play together again!")
    friendship = manager.play_together(leo, glenn, 10)
    print(manager.draw_cats_together(leo, glenn))
    print(f"Friendship after more play: {friendship.score}")

    print("\nFinal friendship status:")
    print(manager.get_friendship(leo, glenn).score)

if __name__ == "__main__":
    main()
