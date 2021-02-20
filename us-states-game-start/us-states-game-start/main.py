import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
screen.screensize()

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
game_is_on = True
states_right = 0

state_data = pandas.read_csv("50_states.csv")
found_states = []
while game_is_on:
    user_answer = screen.textinput(title=f"Guess A State: {states_right}/50", prompt="What's a state on the map?")

    if user_answer.lower() == "exit":
        game_is_on = False
    if user_answer in found_states:
        continue
    for states in state_data["state"]:
        if user_answer.lower() == states.lower():
            found_states.append(states.lower())
            text = turtle.Turtle()
            text.hideturtle()
            text.penup()

            x_cor = int(state_data[state_data.state == states]["x"])
            y_cor = int(state_data[state_data.state == states]["y"])

            text.goto(x_cor, y_cor)
            text.write(states, align="center", font=("Ariel", 7, "bold"))

            states_right += 1
    if states_right == 50:
        game_is_on = False

states_to_learn = {
    "Missing States": []
}
for states in state_data["state"]:
    if states.lower() not in found_states:
        states_to_learn["Missing States"].append(states)

missing_states = pandas.DataFrame(states_to_learn)
missing_states.to_csv("states_to_learn")

screen.exitonclick()
