def start_game():
    print("\nWelcome to Adventure Game!")

    choice1 = input("You are at a crossroad. Go left or right? ").lower()

    if choice1 == "left":
        river()
    elif choice1 == "right":
        print("You fell into a hole. Game over!")
    else:
        print("Invalid choice!")


def river():
    choice2 = input("You see a river. Swim or wait? ").lower()

    if choice2 == "wait":
        print("You found treasure! You win!")
    elif choice2 == "swim":
        print("Crocodile attack! Game over!")
    else:
        print("Invalid choice!")


while True:
    start_game()

    again = input("Play again? (y/n): ").lower()

    if again != "y":
        break