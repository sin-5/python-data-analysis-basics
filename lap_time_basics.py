lap_times = {1: 92.4, 2: 91.8, 3: 93.1, 4: 91.6, 5: 92.0}

for lap in lap_times:
    print('Lap', lap, lap_times[lap])

#print('Average:', sum(lap_times) / len(lap_times))
def average_lap_time(lap_times):
    total = 0
    for lap in lap_times:
        total += lap_times[lap]
    return total / len(lap_times)

print('Average:', average_lap_time(lap_times))

def find_fastest_lap(lap_times):
    fastest = lap_times[1]
    fastest_lap = 1
    for lap in lap_times:
        if fastest >= lap_times[lap]:
            fastest = lap_times[lap]
            fastest_lap = lap
    return fastest, fastest_lap

fastest = find_fastest_lap(lap_times)
print('Fastest:', fastest[0], 'Lap:', fastest[1])

def display_laps_under_92(lap_times):
    for lap in lap_times:
        if lap_times[lap] < 92:
            print('Lap', lap, ':', lap_times[lap])

display_laps_under_92(lap_times)