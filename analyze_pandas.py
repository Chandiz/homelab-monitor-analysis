import pandas as pd

log_file = "system_log.csv"

# Read the CSV into a DataFrame
df = pd.read_csv(log_file)

# Print the entire DataFrame
print(df)

# Print summary statistics
print(df.describe())
