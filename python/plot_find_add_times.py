import numpy as np
import matplotlib.pyplot as plt
from tools import get_array, dags

data = dags[0]

find_or_add_time = get_array(data, "find_or_add time")
find_or_add_add = get_array(data, "find_or_add add")
find_or_add_level = get_array(data, "find_or_add level")

indices_add = find_or_add_add == 1
indices_noadd = find_or_add_add == 0

print("Num add: ", np.sum(indices_add))
print("Num no add: ", np.sum(indices_noadd))

assert np.sum(indices_add) + np.sum(indices_noadd) == len(find_or_add_time)

plot_index = 0
for level in range(32):
    level_indices = level == find_or_add_level
    if np.sum(level_indices) == 0:
        continue

    plot_index += 1
    plt.subplot(2, 3, plot_index)
    plt.xlabel("time (ms)")
    plt.ylabel("count (log)")
    plt.yscale("log")
    plt.title("level = " + str(level))
    plt.hist(find_or_add_time[np.logical_and(indices_noadd, level_indices)], bins=100)
plt.show()