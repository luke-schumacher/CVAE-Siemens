import matplotlib.pyplot as plt
from pandas.plotting import table
import pandas as pd

# Define your data
body1_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "haste", "qDWI", "resolve", "space", "svs_se", "svs_st", "tse"]
body2_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "haste", "qDWI", "resolve", "space", "svs_se", "svs_st", "tfl_b1map"]
body3_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "haste", "qDWI", "resolve", "space", "svs_se", "svs_st", "tfl", "tfl_b1map"]
body4_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "haste", "qDWI", "resolve", "svs_se"]
body5_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "haste", "qDWI", "resolve", "svs_se"]

# Find the maximum length among all arrays
max_length = max(len(body1_data), len(body2_data), len(body3_data), len(body4_data), len(body5_data))

# Fill arrays with "N/A" for missing values
body1_data += ["none"] * (max_length - len(body1_data))
body2_data += ["none"] * (max_length - len(body2_data))
body3_data += ["none"] * (max_length - len(body3_data))
body4_data += ["none"] * (max_length - len(body4_data))
body5_data += ["none"] * (max_length - len(body5_data))

# Create a dataframe
df = pd.DataFrame({
    "Body 1": body1_data,
    "Body 2": body2_data,
    "Body 3": body3_data,
    "Body 4": body4_data,
    "Body 5": body5_data
})

# Plot the table with title
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('off')
tbl = table(ax, df, loc='center', colWidths=[0.2]*len(df.columns))
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
tbl.scale(1.1, 1.1)  # Adjust the table size if needed

# Save the figure
plt.savefig('table_image.png', bbox_inches='tight')
plt.show()
