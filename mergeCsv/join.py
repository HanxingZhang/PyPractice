import pandas as pd

# inner join
data1 = pd.read_csv('../Data/loan.csv')
data2 = pd.read_csv('../Data/borrower.csv')
output1 = pd.merge(data1, data2, on='LOAN_NO', how='inner')
# output1.to_csv(r'..\Data\output1.csv', index = False, header = True)

# Left Outer Join
output2 = pd.merge(data1, data2,
                   on='LOAN_NO',
                   how='left')
print(output2)

# how: {‘left’, ‘right’, ‘outer’, ‘inner’}, default ‘inner’
# on: label or list