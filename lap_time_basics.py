lap_times = [92.4, 91.8, 93.1, 91.6, 92.0]

for i in range(len(lap_times)):
    print('Lap', i + 1, lap_times[i])

#print('Average:', sum(lap_times) / len(lap_times))
total = 0
for i in range(len(lap_times)):
    total += lap_times[i]
average = total / len(lap_times)
print('Average:', average)

fastest = lap_times[0]
fastest_lap = 1
for i in range(len(lap_times)):
    if fastest >= lap_times[i]:
        fastest = lap_times[i]
        fastest_lap = i + 1
print('Fastest:', fastest, 'Lap:', fastest_lap)
