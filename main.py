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
import pandas
data=pandas.read_csv('Squirrel_Data.csv')
grey_squirrel_count=len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count=len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count=len(data[data["Primary Fur Color"] == "Black"])
data_count={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_squirrel_count,black_squirrel_count,black_squirrel_count]
}
data_frame=pandas.DataFrame(data_count)
data_frame.to_csv("squirrel_count.csv")
