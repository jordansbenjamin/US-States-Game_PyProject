import turtle
import pandas

FONT = ('Arial', 10, 'normal')

states_csv = "50_states.csv"

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
# screen.setup(width=724, height=494)
screen.setup(width=726, height=496)
screen.addshape(image)

image_ob = turtle.Turtle()
image_ob.shape(image)
writing_ob = turtle.Turtle()

data = pandas.read_csv(states_csv)
states = data.state.tolist()
# print(data.loc[data.state == "Ohio", ['x', 'y']].values.flatten().tolist())
# print(states)

def write_state(user_guess, coordinates):
    writing_ob.penup()
    writing_ob.hideturtle()
    writing_ob.color('black')
    writing_ob.goto(x=coordinates[0], y=coordinates[1])
    writing_ob.write(user_guess, align='center', font=FONT)

score = 0

while True:
    score_tally = f"{score}/50 States Correct"
    answer_state = screen.textinput(title=score_tally, prompt="What's another state's name?")
    user_guess = answer_state.title()
    # print(type(user_guess))
    coordinates = data.loc[data.state == user_guess, ['x', 'y']].values.flatten().tolist()

    if user_guess in states:
        score += 1
        write_state(user_guess, coordinates)
        # print("correct")
        


screen.exitonclick()

# To get coordinates using mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()