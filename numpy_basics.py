import numpy as np

lap_times = [92.4, 91.8, 93.1, 91.6, 92.0]

lap_times_array = np.array(lap_times)
print('Average:', f'{np.average(lap_times_array):.2f}')
print('Min:', np.min(lap_times_array))
print('Max:', np.max(lap_times_array))
print('Under 92:', lap_times_array[lap_times_array < 92])