import  turtle
import pandas

screen = turtle.Screen()
screen.title("U.S Stats Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
tim = turtle.Turtle()
tim.color("black")
tim.penup()
tim.hideturtle()


data = pandas.read_csv("50_states.csv")
list_of_correct_guesses = []
list_of_states = data.state.tolist()
while len(list_of_correct_guesses) < 50:

    answer_state = screen.textinput(title= f"Guess the state: {len(list_of_correct_guesses)}/50", prompt="Whats another state's name?").title()
    if answer_state == "Exit":
        mis_state_list = [state for state in list_of_states if state not in list_of_correct_guesses]
        # for state in list_of_states:
        #     if state not in list_of_correct_guesses:
        #         mis_state_list.append(state)
        new_data = pandas.DataFrame(mis_state_list)
        new_data.to_csv("missin_states.csv")
        break
    if answer_state in list_of_states:
        list_of_correct_guesses.append(answer_state)
        row = data[data.state == answer_state]
        tim.goto(row.x.item(),row.y.item())
        tim.write(f"{row.state.item()}", font=("ariel", 12, "normal"))







