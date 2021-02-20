import turtle
import pandas

#Create the window for the game
screen = turtle.Screen()
screen.title("US State Game")
screen.screensize()

#Image of the US map for the background
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
game_is_on = True #Boolean to keep the game running in a while loop
states_right = 0 #Variable to keep track of states the user got right

state_data = pandas.read_csv("50_states.csv") #Read a csv of all the 50 states
found_states = [] #List to keep track of the states named correctly
while game_is_on:
    user_answer = screen.textinput(title=f"Guess A State: {states_right}/50", prompt="What's a state on the map?") #Text bok for user to input a state

    if user_answer.lower() == "exit": #If user inputs "exit" game closes
        game_is_on = False
        continue
    if user_answer in found_states: #If user names a state in the list of found states then they get to try again (no penalty)
        continue
    for states in state_data["state"]: #If state is in the csv of states
        if user_answer.lower() == states.lower(): #If user input matches a state in the csv list. Makes user input and input from csv lowercase
            found_states.append(states.lower()) #Add state to found states
            text = turtle.Turtle() #Creates a Turtle to add text to
            text.hideturtle() #Hides lines of the turtle and the turtle
            text.penup()

            x_cor = int(state_data[state_data.state == states]["x"]) #Gets coordinates from states csv
            y_cor = int(state_data[state_data.state == states]["y"])

            text.goto(x_cor, y_cor) #Uses coordinates in the csv to place the turtle text bot at the correct part of the map
            text.write(states, align="center", font=("Ariel", 7, "bold")) #Writes state on the window

            states_right += 1 #Correct states count goes up 1
    if states_right == 50: #If all states found (count = 50) game ends
        game_is_on = False

states_to_learn = { #Create a dictionary to add the missing states to
    "Missing States": []
}
for states in state_data["state"]: #Goes through all the states in the csv
    if states.lower() not in found_states: #If the state is not in the found_states list from the game
        states_to_learn["Missing States"].append(states) #Add the state to the dictionary of missing states

missing_states = pandas.DataFrame(states_to_learn) #Create a file to store dictionary in
missing_states.to_csv("states_to_learn") #Turn data frame to a csv

screen.exitonclick() #Keeps window open
