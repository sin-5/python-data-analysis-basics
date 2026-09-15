lap_times = {
    1: 92.4,
    2: 91.8,
    3: 93.1,
    4: 91.6,
    5: 92.0 
}

with open('lap_times.txt', 'w') as f:
    for lap_num, lap_time in lap_times.items():
        f.write(f'Lap {lap_num}: {lap_time}\n')

with open('lap_times.txt', 'r') as f:
    print(f.read())