# # import csv
# # with open("weather_data.csv") as data:
# #     read_csv=csv.reader(data)
# #     temperatures=[]
# #     for row in read_csv:
# #         if row[1]!="temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
# import pandas
# import  math
# data=pandas.read_csv('weather_data.csv')
# excel_data=data.to_dict()
# # print(excel_data)
# # list_data=data.temp
# # sum=0
# # av=list_data.mean()
# # print(av)
# print(data[data.day == "Monday"])
# # for temp in list_data:
# #     sum+=temp
# # average=round(sum/len(list_data),2)
# # print(average)
#
# # print(list_data)
# import pandas
# data=pandas.read_csv('Squirrel_Data.csv')
# grey_squirrel_count=len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrel_count=len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count=len(data[data["Primary Fur Color"] == "Black"])
# data_count={
#     "Fur Color":["Gray","Cinnamon","Black"],
#     "Count":[grey_squirrel_count,black_squirrel_count,black_squirrel_count]
# }
# data_frame=pandas.DataFrame(data_count)
# data_frame.to_csv("squirrel_count.csv")
import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.setup(500, 500)

correct_guess = []
missing_state = []  # Initialize the list to store missing states
data = pandas.read_csv("50_states.csv")
list_data = data["state"].to_list()

while True:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/{len(list_data)} States Correct", prompt="What is another State's name?").title()
    if answer_state == "Exit":
        # Collect missing states
        missing_state=[state for state in list_data if state not in correct_guess]
        # for state in list_data:
        #     if state not in correct_guess:
        #         missing_state.append(state)
        missing_state_data = pandas.DataFrame(missing_state, columns=["States"])
        missing_state_data.to_csv("states_to_learn.csv", index=False)
        break
    if answer_state in list_data:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        correct_guess.append(answer_state)
        t.write(answer_state)
    else:
        print("no")
    print(correct_guess)
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
# screen.exitonclick()
