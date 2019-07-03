thy = input()
import turtle
wn = turtle.Screen()
wn.bgcolor("#E0FFFF")
thuy = turtle.Turtle()
thuy.color("blue")
if type(thy) == str and thy =="a":
    thuy.forward(100)
elif type(thy) == str and thy != "a":
    thuy.right(100)
    thuy.forward(100)
else:
    print("Please enter a string and try back!")
wn.exitonclick()
