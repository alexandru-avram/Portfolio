from turtle import Turtle
from tkinter import messagebox
from pathlib import Path
score_alignment = "center"
score_font = ("Arial", 24, "normal")

# This is how you get the current folder of this file
HERE = Path(__file__).resolve().parent


class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 450)
        self.hideturtle()

        self.score = 0

        # Open the file high_score.txt where we will store the highest score
        try:
            with open("high_score.txt") as saved_score:
                self.high_score = int(saved_score.read().strip())
        except (FileNotFoundError, ValueError):
            self.high_score = 0  # default if file empty or missing


        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=score_alignment, font=score_font)

    def inscrease_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def reset(self):
        self.clear()
        if self.score > self.high_score:
            messagebox.showinfo("NEW HIGH SCORE !!!", f"Your score was {self.score}")

            with open("high_score.txt", mode = "w") as saved_score:
                saved_score.write(f"{self.score}")

            self.high_score = self.score
        else:
            messagebox.showinfo("ROUND OVER", f"Your score was {self.score}")
        self.score = 0
        self.update_scoreboard()
        
        