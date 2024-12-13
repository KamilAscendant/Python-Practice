import random

def revolver(chambers):
    return random.randint(1, chambers)

def play_game():
    chambers= 6
    while chambers > 1:
        print(f"Squeezing the trigger! {chambers} chambers left.")
        result = revolver(chambers)
        if result == 1:
            print("BANG! Game Over")
            return
        else:
            print(f"Click. Safe for now.")
            chambers -= 1
    print("Congratulations! You lived... for now")

if __name__ == "__main__":
    play_game()