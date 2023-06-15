import turtle
import pandas

states_csv = "50_states.csv"

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
# screen.setup(width=724, height=494)
screen.setup(width=726, height=496)
screen.addshape(image)

image_ob = turtle.Turtle()
image_ob.shape(image)

data = pandas.read_csv(states_csv)
states = data.state.tolist()
# print(states)

score = 0
score_tally = f"{score}/50 States Correct"

while True:
    answer_state = screen.textinput(title=score_tally, prompt="What's another state's name?")
    user_guess = answer_state.title()
    print(user_guess)

    if user_guess in states:
        print("correct")


screen.exitonclick()

# To get coordinates using mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()