from random import choice
from random import randint
from tkinter import *
from tkinter import ttk
from turtle import Screen
from turtle import Turtle


def show_result(result):
    """ Shows a pop-up with the result of the match """
    root = Tk()
    frm = ttk.Frame(root, padding=50)
    frm.grid()
    ttk.Label(frm, text=result).grid(column=0, row=0)
    root.mainloop()


screen = Screen()

screen.setup(width=800, height=600)
user_bet = screen.textinput(title='Make your bet',
                            prompt='Which turtle will win the race? Enter the color: ')
colors = ['red', 'orange', 'black', 'green', 'blue', 'purple']
all_turtles_list = list()


def create_turtles():
    """ Creating the turtles """

    y = -225
    x = -375

    for i in range(0, 6):
        y += 65
        new_turtle = Turtle(shape='turtle')
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(x=x, y=y)
        all_turtles_list.append(new_turtle)

    make_race()


def make_race():
    """ Turtle race animation """

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles_list:
            if turtle.xcor() > 380:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    show_result("You've won!")
                    screen.bye()

                else:
                    show_result("You've lost!")
                    screen.bye()

            random_distance = randint(0, 10)
            turtle.forward(random_distance)


create_turtles()

screen.exitonclick()
