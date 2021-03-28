import pandas as pd
import copy

df = pd.read_csv('./Data/dirtydata.csv')

# Empty Cells
# Remove Rows: By Default, the dropna() method returns a new DataFrame, and will not change the original
new_df = df.dropna()
#print(new_df.to_string())

# the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containg NULL values from the original DataFrame.
df_2 = copy.deepcopy(df)
df_2.dropna(inplace = True)
#print(df_2.to_string())

# Replace Empty Values
df_3 = copy.deepcopy(df)
df_3.fillna(130, inplace=True)
# print(df_3.to_string())

# Replace Only For a Specified Columns
df_4 = copy.deepcopy(df)
df_4['Calories'].fillna(130, inplace=True)
# print(df_4.to_string())

# Replace Using Mean, Median, or Mode
df_5 = copy.deepcopy(df)
x = df["Calories"].mean()
y = df["Calories"].median()
# Mode = the value that appears most frequently.
z = df["Calories"].mode()[0]
df_5["Calories"].fillna(x, inplace = True)

# Data of Wrong Format
# Convert Into a Correct Format
df_6 = copy.deepcopy(df)
df_6['Date'] = pd.to_datetime(df_6['Date'])
# print(df_6.to_string())
df_6.dropna(subset=['Date'], inplace = True)

# Wrong Data
# Replacing Values
df_7 = copy.deepcopy(df)
#df_7.loc[7, 'Duration'] = 45
for x in df_7.index:
    if df_7.loc[x, 'Duration'] > 120:
        df_7.loc[x, 'Duration'] = 120
        # df_7.drop(x, inplace = True)
# print(df_7)

# Removing Duplicates
# The duplicated() method returns a Boolean values for each row:
print(df.duplicated())
df_7.drop_duplicates(inplace = True)
