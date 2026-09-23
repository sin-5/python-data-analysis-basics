import pandas as pd

df = pd.read_csv('lap_times.csv')

print(df, '\n')
print('Average:', f'{df['lap_time'].mean():.2f}')
print('Min:', df['lap_time'].min(), '\n')
print('Under 92:\n', df[df['lap_time'] < 92])
