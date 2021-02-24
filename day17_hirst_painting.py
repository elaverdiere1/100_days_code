import turtle as t
import random
# creating a list of colors using an image and colorgram
# import colorgram
#
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
#
# for x in colors:
#     r = x.rgb.r
#     g = x.rgb.g
#     b = x.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(141, 84, 62), (195, 167, 86), (69, 82, 115), (221, 213, 104), (203, 94, 64), (193, 123, 147), (125, 192, 168), (136, 63, 78), (115, 159, 182), (167, 173, 60), (66, 137, 93), (100, 156, 102), (53, 54, 105), (98, 142, 148), (198, 100, 152), (51, 71, 69), (151, 206, 208), (153, 207, 194), (81, 55, 80), (106, 121, 163), (222, 180, 168), (216, 177, 186), (84, 56, 56), (68, 60, 52), (185, 187, 206), (71, 65, 54)]

# creating the screen and turtle object to make the painting
turt = t.Turtle()
t.colormode(255)
screen = t.Screen()
screen.screensize(500, 500)
screen.setworldcoordinates(0, 0, 11, 11)

# line of dots
def create_dot_line():
    for _ in range(10):
        turt.dot(20, random.choice(color_list))
        turt.forward(1)


turt.penup()
turt.hideturtle()
turt.speed(0)

# creating a square of dots by repeating lines
for y in range(11):
    turt.setposition(0.5, y + 0.5)
    create_dot_line()

screen.exitonclick()
