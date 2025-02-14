# import csv
# with open("weather_data.csv") as data:
#     read_csv=csv.reader(data)
#     temperatures=[]
#     for row in read_csv:
#         if row[1]!="temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas
import  math
data=pandas.read_csv('weather_data.csv')
excel_data=data.to_dict()
# print(excel_data)
# list_data=data.temp
# sum=0
# av=list_data.mean()
# print(av)
print(data[data.day == "Monday"])
# for temp in list_data:
#     sum+=temp
# average=round(sum/len(list_data),2)
# print(average)

# print(list_data)