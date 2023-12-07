import matplotlib.pyplot as plt
from pandas.plotting import table
import pandas as pd

# Your knee data
knee_175608 = ["Seq_gre", "Seq_gre", "Seq_tse", "Seq_tse", "Seq_tse", "Seq_tse", "Seq_tse", "Seq_tse"]
knee_182627 = ["Seq_AALScout", "Seq_tse", "Seq_tse_dixon", "Seq_tse_dixon", "Seq_tse", "Seq_fl3d_vibe", "Seq_tse_dixon", "Seq_fl3d_vibe", "Seq_haste"]
knee_202531 = ["Seq_AALScout", "Seq_tse", "Seq_space", "Seq_tse", "Seq_tse", "Seq_tse", "Seq_tse"]

# Find the maximum length among all arrays
max_length = max(len(knee_175608), len(knee_182627), len(knee_202531))

# Fill arrays with "N/A" for missing values
knee_175608 += ["none"] * (max_length - len(knee_175608))
knee_182627 += ["none"] * (max_length - len(knee_182627))
knee_202531 += ["none"] * (max_length - len(knee_202531))

# Create a dataframe
df = pd.DataFrame({
    "Knee 175608": knee_175608,
    "Knee 182627": knee_182627,
    "Knee 202531": knee_202531
})

# Plot the table with title
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('off')
tbl = table(ax, df, loc='center', colWidths=[0.2]*len(df.columns))
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
tbl.scale(1.1, 1.1)  # Adjust the table size if needed

# Save the figure
plt.savefig('knee_table.png', bbox_inches='tight')
plt.show()
