# import csv
# with open("weather_data.csv") as data:
#     read_csv=csv.reader(data)
#     temperatures=[]
#     for row in read_csv:
#         if row[1]!="temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas
data=pandas.read_csv("weather_data.csv")
print(data["temp"])
