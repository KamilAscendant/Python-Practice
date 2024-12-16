import random

def revolver(chambers):
    return random.randint(1, chambers)

def play_game():
    chambers = 6
    try:
        shots = int(input("How many times do you want to shoot? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    while shots > 0 and chambers > 1:
        print(f"Squeezing the trigger! {chambers} chambers left.")
        result = revolver(chambers)
        if result == 1:
            print("BANG! Game Over")
            return
        else:
            print(f"Click. Safe for now.")
            chambers -= 1
            shots -= 1

    if chambers == 1:
        print("Congratulations! You lived... for now")
    else:
        print("You survived the number of shots you chose.")

if __name__ == "__main__":
    play_game()