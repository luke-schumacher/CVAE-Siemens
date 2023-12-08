import matplotlib.pyplot as plt
from pandas.plotting import table
import pandas as pd

# Load knee data from three separate CSV files
df_175608 = pd.read_csv('model_results/175608/brain_175608.csv', header=None)
df_182627 = pd.read_csv('model_results/182627/brain_182627.csv', header=None)
df_202531 = pd.read_csv('model_results/202531/brain_202531.csv', header=None)

# Find the maximum length among all arrays
max_length = max(
    df_175608.applymap(lambda x: len(str(x))).max().max(),
    df_182627.applymap(lambda x: len(str(x))).max().max(),
    df_202531.applymap(lambda x: len(str(x))).max().max()
)

# Convert each column to a list of strings
df_175608 = df_175608.astype(str)
df_182627 = df_182627.astype(str)
df_202531 = df_202531.astype(str)

# Fill arrays with "none" for missing values
df_175608 = df_175608.apply(lambda col: col.tolist() + ["none"] * (max_length - len(col)))
df_182627 = df_182627.apply(lambda col: col.tolist() + ["none"] * (max_length - len(col)))
df_202531 = df_202531.apply(lambda col: col.tolist() + ["none"] * (max_length - len(col)))

# Create a combined dataframe
df_combined = pd.DataFrame({
    "Brain 175608": df_175608[0],
    "Brain 182627": df_182627[0],
    "Brain 202531": df_202531[0]
})

# Trim the dataframe to the desired number of rows
df_combined = df_combined.iloc[:8]

# Plot the table with title
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('off')
tbl = table(ax, df_combined, loc='center', colWidths=[0.2]*len(df_combined.columns))
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
tbl.scale(1.1, 1.1)  

# Save the figure
plt.savefig('plotting/plot_results/brain_table.png', bbox_inches='tight')
plt.show()
