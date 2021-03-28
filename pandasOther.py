import pandas as pd
import matplotlib.pyplot as plt

# Plotting
df = pd.read_csv('./Data/data.csv')

df.plot()

plt.show()