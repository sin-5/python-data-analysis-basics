import csv

lap_times = {
    1: 92.4,
    2: 91.8,
    3: 93.1,
    4: 91.6,
    5: 92.0
}

with open('lap_times.csv', 'w', newline='') as f:
    fieldnames = ['lap', 'lap_time']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for lap_num, lap_time in lap_times.items():
        writer.writerow({'lap':lap_num, 'lap_time':lap_time})

with open('lap_times.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['lap'], row['lap_time'])
