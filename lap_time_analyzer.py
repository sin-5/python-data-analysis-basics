import pandas as pd
import matplotlib.pyplot as plt

def read_csv():
    df = pd.read_csv('lap_times.csv')
    return df

def average(df):
    average = df['lap_time'].mean()
    return average

def fastest(df):
    fastest_index = df['lap_time'].idxmin()
    fastest_lap = df.loc[fastest_index, 'lap']
    fastest_lap_time = df['lap_time'].min()
    return fastest_lap, fastest_lap_time

def under_92(df):
    under_92 = df[df['lap_time'] < 92]
    return under_92

def graph(df):
    plt.plot(df['lap'], df['lap_time'])
    plt.xlabel('Lap Number')
    plt.ylabel('Lap Time')
    plt.title('lap_times.csv')
    plt.show()

df = read_csv()
print('Average:', f'{average(df):.2f}')
fastest_lap, fastest_lap_time = fastest(df)
print('Fastest Lap: Lap', fastest_lap, '-', fastest_lap_time, 'sec')
print('Under 92 sec:\n', under_92(df))
graph(df)
