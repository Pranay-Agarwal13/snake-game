from turtle import Turtle
import os

HIGH_SCORE_FILE = "high_score.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x=0, y=260)
        self.color("white")
        self.hideturtle()
        self.high_score = self._load_high_score()
        self.update_score()

    def _load_high_score(self):
        if not os.path.exists(HIGH_SCORE_FILE):
            return 0
        try:
            with open(HIGH_SCORE_FILE, "r") as f:
                return int(f.read().strip() or 0)
        except Exception:
            return 0

    def _save_high_score(self):
        try:
            with open(HIGH_SCORE_FILE, "w") as f:
                f.write(str(self.high_score))
        except Exception:
            pass

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High score: {self.high_score}", align="center", font=("Arial", 18, "normal"))

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self._save_high_score()
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            self._save_high_score()
        self.update_score()

    def reset(self):
        self.score = 0
        self.update_score()
        self.goto(0, 260)
