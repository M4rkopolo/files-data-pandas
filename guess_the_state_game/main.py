from turtle import Turtle, Screen
import pandas

us_states = pandas.read_csv("50_states.csv")
us_states_dict = us_states.to_dict()        #saving df to dict 
screen = Screen()
screen.bgpic("blank_states_img.gif")        #using img in the background
correct_guess = []
states_to_learn = []
while len(correct_guess) < 50:
    user_input = screen.textinput(f"{len(correct_guess)}/50 States Correct", "Write names of US states one by one: ")
    for index in range(0, 49):
        if user_input.lower() == us_states_dict["state"][index].lower():    #checking if user input is correct
            new_state = Turtle()                                            #each name of the guessed state name has an instance to write to that name
            new_state.penup()
            new_state.hideturtle()
            new_state.goto(int(us_states_dict["x"][index]), int(us_states_dict["y"][index]))    #each state has coordinates, the key to them is the state name
            new_state.write(f"{us_states_dict['state'][index]}", True, align="center")          #drawing the name of state
            if us_states_dict["state"][index] not in correct_guess:
                correct_guess.append(us_states_dict["state"][index])                            #appending guessed name to list
    if user_input == "exit":
        break
for state in range(0, 49):
    if us_states_dict["state"][state] not in correct_guess:                                     #appending all not guessed state names to the learning list
        states_to_learn.append(us_states_dict["state"][state])
result = pandas.DataFrame(states_to_learn)
result.to_csv('states_to_learn.csv')
screen.exitonclick()
