import matplotlib.pyplot as plt
from pandas.plotting import table
import pandas as pd

# Your data
Turkey_Amira_brain = ["AALScout", "tse", "tse", "dess", "none", "none", "none", "none", "none", "none"]
Germany_VIDA_brain = ["AALScount", "tse", "tse", "tse", "tse", "tse", "tse", "none", "none", "none"]
China_VIDA_brain = ["gre", "gre", "tse", "tse", "tse", "tse", "tse", "tse", "tse", "tse"]

# Create a combined dataframe
df_combined_brain = pd.DataFrame({
    "Turkey Amira Brain": Turkey_Amira_brain,
    "Germany VIDA Brain": Germany_VIDA_brain,
    "China VIDA Brain": China_VIDA_brain
})

# Plot the table with title
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('off')
tbl = table(ax, df_combined_brain, loc='center', colWidths=[0.2]*len(df_combined_brain.columns))
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
tbl.scale(1.1, 1.1)  

# Save the figure
#plt.savefig('plotting/plot_results/brain_table.png', bbox_inches='tight')
plt.show()
