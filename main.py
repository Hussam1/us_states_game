import pandas as pd
import turtle

screen = turtle.Screen()
picture = "blank_states_img.gif"
screen.addshape(picture)
turtle.shape(picture)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_state = []

while len(guess_state) < 50:
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 states",
                                    prompt="what is your next state guess?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guess_state:
                missing_states.append(state)
        missing_df = pd.DataFrame(missing_states)
        missing_df.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_info = data[data.state == answer_state]
        t.goto(int(state_info.x), int(state_info.y))
        t.write(answer_state)
