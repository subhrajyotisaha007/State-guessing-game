from turtle import Turtle, Screen
import pandas


turtle = Turtle()
image = 'blank_states_img.gif'
screen = Screen()
screen.title('us state guessing game')
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv('50_states.csv')
state_list = data['state'].to_list()
guessed_states = []
new = []
while len(guessed_states)<50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 states correct',prompt='make a state name').capitalize()
    if answer_state == 'Exit':
        for each in state_list:
            if each not in guessed_states:
                new.append(each)
        print(new)
        new_data = pandas.DataFrame(new)
        new_data.to_csv('rest of the states.csv')
        break
    if answer_state in state_list:
        guessed_states.append(answer_state)
        names = Turtle()
        names.hideturtle()
        names.penup()
        row = data[data['state'] == answer_state]
        names.goto(int(row.x),int(row.y))
        names.write(row.state.item())
