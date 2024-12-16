import random

def revolver(chambers):
    return random.randint(1, chambers)


def play_game():
    points = 0
    lives = 3

    while lives > 1:
        chambers = 6
        score = 0
        try:
            shots = int(input(f"You have {lives} lives left! How many times do you want to shoot? "))
            if shots == 0:
                print("You're no fun. Game Over.")
                print(f"Your final score is {points}")
                break 
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        while shots > 0 and chambers > 1:
            print(f"Squeezing the trigger! {chambers} chambers left.")
            result = revolver(chambers)
            if result == 1 and lives != 1:
                print("BANG! You lost a life")
                lives -= 1
                score = 0
                break
            elif lives == 1 and result == 1:
                print("BANG! You lost your last life")
                print("Game Over")
                score = 0
                break
            else:
                print(f"Click. Safe for now.")
                chambers -= 1
                shots -= 1
                score += 1

        if chambers == 1:
            print("Congratulations! There really was... heh... ONE in the chamber.")
            points = points + score + 3
            print(f"Your score is {points}")
        else:
            print("Good on you, knowing when to quit :p")
            points += score
            print(f"Your score is {points}")

if __name__ == "__main__":
    play_game()