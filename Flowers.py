#Author: Thy H. Nguyen

thy = input()
# This is the place for user to input anything (a string, a number, or a boolean)
import turtle

# Set up turtle to draw
wn = turtle.Screen()
# Set up the screen of the turtle
wn.bgcolor("#E0FFFF")
# Set up the background color of the turtle
thuy = turtle.Turtle()
# Set up the turtle with the name "thuy"
thuy.color("blue")
# Set up the turtle's color
if thy == "a":
    thuy.forward(100)
# If the user input the string "a", it will draw a straight line
else:
    thuy.begin_fill()
    for i in range(10):
        thuy.right(360 / 10)
        thuy.forward(100)
    thuy.end_fill()
# If the input is not "a", it will draw the decagon)

wn.exitonclick()
# Set up the screen so that it will exit when the user clicks
