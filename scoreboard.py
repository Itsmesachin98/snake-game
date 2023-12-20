from turtle import Turtle

FONT = ("courier", 16, "bold")

class Scoreboard:
    def __init__(self):
        self.point = 0
        self.highscore()
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.color("white")
        self.turtle.goto(0, 270)
        self.score()        

    def score(self):
        self.turtle.write(f"Score: {self.point} || Highscore: {self.highest_point}", align="center", font=FONT)

    def highscore(self):
        with open("highscore.txt", "r") as f:
            self.highest_point = f.read()
    
    def increase_score(self):
        self.point += 1
        self.turtle.clear()
        self.score()

    def game_over(self):
        self.turtle.goto(0, 0)
        self.turtle.write("GAME OVER!", align="center", font=FONT)

        if self.point > int(self.highest_point):
            with open("highscore.txt", "w") as f:
                f.write(str(self.point))

    