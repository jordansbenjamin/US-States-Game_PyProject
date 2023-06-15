import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
# screen.setup(width=724, height=494)
screen.setup(width=726, height=496)
screen.addshape(image)

image_ob = turtle.Turtle()
image_ob.shape(image)



while True:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    user_guess = answer_state.title()


screen.exitonclick()

# To get coordinates using mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()