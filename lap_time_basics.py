lap_times = [92.4, 91.8, 93.1, 91.6, 92.0]

for i in range(len(lap_times)):
    print('Lap', i + 1, lap_times[i])

#print('Average:', sum(lap_times) / len(lap_times))
SUM = 0
for i in range(len(lap_times)):
    SUM += lap_times[i]
AVERAGE = SUM / len(lap_times)
print('Average:', AVERAGE)