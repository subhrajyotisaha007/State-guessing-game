from turtle import Turtle, Screen
import pandas


turtle = Turtle()
image = 'blank_states_img.gif'
screen = Screen()
screen.title('us state guessing game')
screen.addshape(image)
turtle.shape(image)

# names = Turtle()
# names.hideturtle()
# names.penup()
# # # def get_cord(x,y):
# # #     print(x,y)
# # #
# # # screen.onscreenclick(get_cord)
# # #
# # # screen.mainloop()
# #
# #
# data = pandas.read_csv('50_states.csv')
# # print(data['state'])
# state_list = data['state'].to_list()
# # print(state_list)
# answer_state = screen.textinput(title='Guess the state',prompt='make a state name')
# for each_state in state_list:
#     if answer_state == each_state:
#         get_in = state_list.index(each_state)
#         row = data[data['state'] == answer_state]
#         # print(row)
#         x_axis = row.x[get_in]
#         # print(x_axis)
#         y_axis = row.y[get_in]
#         # print(y_axis)
#
#         names.goto(x_axis,y_axis)
#         names.write(arg=answer_state,align='center')



# # print(state_list)
# game_on = True
# while game_on:
#     answer_state = screen.textinput(title='Guess the state', prompt='make a state name')
#     for each_state in state_list:
#         if answer_state == each_state:
#             get_in = state_list.index(each_state)
#             state_row = data[data['state'] == answer_state]
#             x_axis = state_row.x[get_in]
#             y_axis = state_row.y[get_in]
#             names.goto(x_axis, y_axis)
#             names.write(arg=answer_state, align='center')
#         if answer_state == 'exit':
#             game_on = False

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
