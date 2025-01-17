from tkinter import Tk, Label, Button, Entry, StringVar, messagebox
import random
from russianroulette import revolver

class RussianRouletteGUI:
    def __init__(self, master):
        self.master = master
        master.title("Russian Roulette Game")

        self.lives = 3
        self.chambers = 6
        self.points = 0
        self.score = 0

        self.lives_label = Label(master, text=f"Lives: {self.lives}")
        self.lives_label.pack()

        self.shots_label = Label(master, text="Enter number of shots:")
        self.shots_label.pack()

        self.shots_entry = Entry(master)
        self.shots_entry.pack()

        self.shoot_button = Button(master, text="Shoot", command=self.shoot)
        self.shoot_button.pack()

        self.result_label = Label(master, text="")
        self.result_label.pack()

    def shoot(self):
        try:
            shots = int(self.shots_entry.get())
            if shots <= 0:
                messagebox.showinfo("Game Over", "You're no fun. Game Over.")
                self.master.quit()
                return
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")
            return

        while shots > 0 and self.chambers > 1:
            result = revolver(self.chambers)
            if result == 1:
                if self.lives > 1:
                    self.lives -= 1
                    self.score = 0
                    self.lives_label.config(text=f"Lives: {self.lives}")
                    self.result_label.config(text="BANG! You lost a life.")
                    break
                else:
                    messagebox.showinfo("Game Over", "BANG! You lost your last life. Game Over.")
                    self.master.quit()
                    return
            else:
                self.result_label.config(text="Click. Safe for now.")
                self.chambers -= 1
                shots -= 1
                self.score += 1

        if self.chambers == 1:
            self.points += self.score + 3
            messagebox.showinfo("Congratulations!", f"You survived! Your score is {self.points}.")
            self.master.quit()
        else:
            self.points += self.score
            self.result_label.config(text=f"Your score is {self.points}. Good on you, knowing when to quit :p")

if __name__ == "__main__":
    root = Tk()
    gui = RussianRouletteGUI(root)
    root.mainloop()