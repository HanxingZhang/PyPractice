import pandas as pd

df = pd.read_csv('./Data/data.csv')
#
# print(df.to_string())

# mydataset = {
#     'cars': ["BMW", "Tesla", "NIO"],
#     'passings': [3, 7, 2]
# }
# myvar = pd.DataFrame(mydataset)
# print(myvar)

# Series: A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type.
a = [1, 7, 2]
serieVar = pd.Series(a)
print(serieVar)
# labels: If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
# This label can be used to access a specified value.
print(serieVar[0])
# Create Labels
serieVar2 = pd.Series(a, index = ['x', 'y', 'z'])
print(serieVar2)
print(serieVar2['y'])
# Key value Objects as Series
calories = {"day1": 420, "day2": 380, "day3": 390}
serieVar3 = pd.Series(calories)
print(serieVar3)
serieVar4 = pd.Series(calories, index=['day1', 'day2'])
print(serieVar4)

# DataFrames: Data sets in Pandas are usually multi-dimensional tables, called DataFrames. whole table
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
# load data into a DataFrame object
dataFrameVar = pd.DataFrame(data)
print(dataFrameVar)
# locate Row: Pandas use the loc attribute to return one or more specified row(s)
print(dataFrameVar.loc[0])
# use a list of indexes:
print(dataFrameVar.loc[[0, 1]])
# named index
dataFrameVar2 = pd.DataFrame(data, index = ['day1', 'day2', 'day3'])
print(dataFrameVar2)
print(dataFrameVar2.loc['day2'])

# Json
dataFrameVar3 = pd.read_json('./Data/data.json')
print(dataFrameVar3.to_string())

# JSON objects have the same format as Python dictionaries
dataJson = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

dataFrameVar4 = pd.DataFrame(dataJson)
print(dataFrameVar4)

# View Data
print(df.head(10))
print(df.head())
print(df.tail())
print(df.info())