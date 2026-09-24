import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('lap_times.csv')

plt.plot(df['lap'], df['lap_time'])
plt.xlabel('Lap Number')
plt.ylabel('Lap time')
plt.title('Lap time Graph')
plt.show()
