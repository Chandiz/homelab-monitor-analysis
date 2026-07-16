import csv
import numpy as np

log_file = "system_log.csv"

with open(log_file, "r", newline="") as f:
    read = csv.reader(f)

    cpu_value = []
    ram_value = []
    disk_value = []

    next(read)

    for row in read:
        cpu_value.append(float(row[1]))
        ram_value.append(float(row[2]))
        disk_value.append(float(row[3]))

cpu_array = np.array(cpu_value)
ram_array = np.array(ram_value)
disk_array = np.array(disk_value)

print("\nAvarage")
print("Avarage CPU:",np.mean(cpu_array))
print("Avarage RAM:",np.mean(ram_array))
print("Avarage DISK:",np.mean(disk_array))

print("\nMaximum")
print("Maximum CPU:",np.max(cpu_array))
print("Maximum RAM:",np.max(ram_array))
print("Maximum DISK:",np.max(disk_array))

print("\nMinimum")
print("Minimum CPU:",np.min(cpu_array))
print("Minimum RAM:",np.min(ram_array))
print("Minimum DISK:",np.min(disk_array))

print("\nStandard Deviation")
print("CPU Std Dev:", np.std(cpu_array))
print("RAM Std Dev:", np.std(ram_array))
print("DISK Std Dev:", np.std(disk_array))
