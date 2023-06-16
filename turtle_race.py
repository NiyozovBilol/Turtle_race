from turtle import Turtle, Screen
import random
from tkinter import messagebox

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter "
                                                          "one of the rainbow colors: ")
print(f"Your choice: {user_bet}")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []
start_pos = -100
for item in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[item])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_pos)
    start_pos += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                messagebox.showinfo(title="Congrats!", message=f"You've won. The {winning_color} turtle is the winner")
            else:
                messagebox.showinfo(title="Woops", message=f"You've lost. The {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
