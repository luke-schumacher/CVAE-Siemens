from tabulate import tabulate

# Define your data
body1_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "haste", "qDWI", "resolve", "space", "svs_se", "svs_st", "tse"]
body2_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "haste", "qDWI", "resolve", "space", "svs_se", "svs_st", "tfl_b1map"]
body3_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "haste", "qDWI", "resolve", "space", "svs_se", "svs_st", "tfl", "tfl_b1map"]
body4_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "haste", "qDWI", "resolve", "svs_se"]
body5_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "qDWI", "resolve", "space", "svs_se", "svs_st"]

# Create a table
table = [
    ["Body 1"] + body1_data,
    ["Body 2"] + body2_data,
    ["Body 3"] + body3_data,
    ["Body 4"] + body4_data,
    ["Body 5"] + body5_data
]

# Display the table
print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))
