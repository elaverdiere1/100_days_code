import turtle
import pandas as pd

screen = turtle.Screen()
screen.tracer(0)
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')

def write_name(state):
    state_name = turtle.Turtle()
    state_name.penup()
    state_name.hideturtle()
    state_name.goto(data[data['state'] == state]['x'].values[0], data[data['state'] == state]['y'].values[0])
    state_name.write(arg=state, align='center', font=('ariel', 12, 'normal'))

correct_states = []
game_continue = True
while game_continue:
    screen.update()
    answer_state = screen.textinput(title=f'{len(correct_states)}/50 States Correct', prompt='What\'s another state\'s name?').title()
    if answer_state in data.values and answer_state not in correct_states:
        write_name(answer_state)
        correct_states.append(answer_state)
    if correct_states == 50:
        game_continue = False
    if answer_state == 'Exit':
        missing_states = []
        for state in data.state.to_list():
            if state not in correct_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break


