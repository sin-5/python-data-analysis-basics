import numpy as np
import pandas as pd

df = pd.read_csv('lap_times.csv')

print(df, '\n')
print('Average:', f'{np.mean(df.lap_time):.2f}')
print('Min:', np.min(df.lap_time), '\n')
print('Under 92:\n', df[df['lap_time'] < 92])
