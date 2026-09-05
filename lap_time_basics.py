lap_times = {1: 92.4, 2: 91.8, 3: 93.1, 4: 91.6, 5: 92.0}

for i in range(len(lap_times)):
    print('Lap', i + 1, lap_times[i + 1])

#print('Average:', sum(lap_times) / len(lap_times))
def average_lap_time(lap_times):
    total = 0
    for i in range(len(lap_times)):
        total += lap_times[i + 1]
    average = total / len(lap_times)
    return average

print('Average:', average_lap_time(lap_times))

def find_fastest_lap(lap_times):
    fastest = lap_times[1]
    fastest_lap = 1
    for i in range(len(lap_times)):
        if fastest >= lap_times[i + 1]:
            fastest = lap_times[i + 1]
            fastest_lap = i + 1
    return fastest, fastest_lap

fastest = find_fastest_lap(lap_times)
print('Fastest:', fastest[0], 'Lap:', fastest[1])

def display_laps_under_92(lap_times):
    for i in range(len(lap_times)):
        if lap_times[i + 1] < 92:
            print('Lap', i + 1, ':', lap_times[i + 1])

display_laps_under_92(lap_times)