import pandas as pd

log_file = "system_log.csv"

# Read the CSV into a DataFrame
df = pd.read_csv(log_file)

# Print the entire DataFrame
print(df)

# Print summary statistics
print(df.describe())

# Filter rows where CPU > 14
high_cpu = df[df["cpu"] > 80]


# Check if any rows matched

if high_cpu.empty:
    print("No CPU warnings")
else:
    print("CPU warnings:")
    print(high_cpu)
