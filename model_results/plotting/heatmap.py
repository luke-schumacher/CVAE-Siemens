import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Function to pad the list with None values
def pad_list(lst, length, pad_value=None):
    return lst + [pad_value] * (length - len(lst))

# Step 1: Data Preparation

# Insert your actual sequence lists for each file here
body1_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "haste", "qDWI", "resolve", "space", "svs_se", "svs_st", "tse"]
body2_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "haste", "qDWI", "resolve", "space", "svs_se", "svs_st", "tfl_b1map"]
body3_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "haste", "qDWI", "resolve", "space", "svs_se", "svs_st", "tfl", "tfl_b1map"]
body4_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "haste", "qDWI", "resolve", "svs_se"]
body5_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "qDWI", "resolve", "space", "svs_se", "svs_st"]

max_length = max(len(body1_data), len(body2_data), len(body3_data), len(body4_data), len(body5_data))

# Pad the lists to the same length
body1_data = pad_list(body1_data, max_length)
body2_data = pad_list(body2_data, max_length)
body3_data = pad_list(body3_data, max_length)
body4_data = pad_list(body4_data, max_length)
body5_data = pad_list(body5_data, max_length)

# Create a dictionary to map sequence names to numerical values
unique_sequences = set(body1_data + body2_data + body3_data + body4_data + body5_data)
sequence_to_number = {seq: i for i, seq in enumerate(unique_sequences)}

# Replace sequence names with numerical values in the data
body1_data = [sequence_to_number[seq] for seq in body1_data]
body2_data = [sequence_to_number[seq] for seq in body2_data]
body3_data = [sequence_to_number[seq] for seq in body3_data]
body4_data = [sequence_to_number[seq] for seq in body4_data]
body5_data = [sequence_to_number[seq] for seq in body5_data]

# Creating a DataFrame
data = {'Body1': body1_data, 'Body2': body2_data, 'Body3': body3_data, 'Body4': body4_data, 'Body5': body5_data}
df = pd.DataFrame(data)

# Step 2: Generate Heatmap
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(df, cmap='Blues', cbar=False, annot=True, fmt='d')

# Step 3: Customize the Plot
plt.title('Sequence Presence Heatmap')
plt.xlabel('BodyParts')
plt.ylabel('Sequences')
plt.show()
