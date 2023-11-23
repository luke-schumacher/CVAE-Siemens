import matplotlib.pyplot as plt
from matplotlib_venn import venn3

body1_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "haste", "qDWI", "resolve", "space", "svs_se", "svs_st", "tse"]
body2_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "haste", "qDWI", "resolve", "space", "svs_se", "svs_st", "tfl_b1map"]
body3_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "haste", "qDWI", "resolve", "space", "svs_se", "svs_st", "tfl", "tfl_b1map"]
body4_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "haste", "qDWI", "resolve", "svs_se"]
body5_data = ["AALScout", "BEAT", "BEAT_FQ", "BEAT_map", "CV_nav", "dess", "ep2d_diff", "ep2d_fid", "fast_tse", "fl3d_ce", "fl3d_vibe", "gre", "gre_field_mapping", "qDWI", "resolve", "space", "svs_se", "svs_st"]

body1_set = set(body1_data)
body2_set = set(body2_data)
body3_set = set(body3_data)
body4_set = set(body4_data)
body5_set = set(body5_data)

venn_labels = {'100': body1_set - body2_set - body3_set - body4_set - body5_set,
               '010': body2_set - body1_set - body3_set - body4_set - body5_set,
               '001': body3_set - body1_set - body2_set - body4_set - body5_set,
               '110': body1_set & body2_set - body3_set - body4_set - body5_set,
               '101': body1_set & body3_set - body2_set - body4_set - body5_set,
               '011': body2_set & body3_set - body1_set - body4_set - body5_set,
               '111': body1_set & body2_set & body3_set - body4_set - body5_set,
               '101': body1_set & body3_set & body5_set - body2_set - body4_set,
               '110': body1_set & body2_set & body4_set - body3_set - body5_set,
               '011': body2_set & body3_set & body5_set - body1_set - body4_set,
               '111': body1_set & body2_set & body3_set & body4_set - body5_set,
               '111': body1_set & body2_set & body3_set & body5_set - body4_set,
               '111': body1_set & body2_set & body4_set & body5_set - body3_set,
               '111': body1_set & body3_set & body4_set & body5_set - body2_set,
               '111': body2_set & body3_set & body4_set & body5_set - body1_set,
               '1001': body1_set & body3_set & body5_set - body2_set - body4_set,
               '1010': body1_set & body2_set & body4_set - body3_set - body5_set,
               '0101': body2_set & body3_set & body5_set - body1_set - body4_set,
               '1100': body1_set & body2_set - body3_set - body4_set - body5_set,
               '0011': body3_set & body5_set - body1_set - body2_set - body4_set,
               '0110': body2_set & body3_set - body1_set - body4_set - body5_set,
               '1000': body1_set - body2_set - body3_set - body4_set - body5_set,
               '0100': body2_set - body1_set - body3_set - body4_set - body5_set,
               '0010': body3_set - body1_set - body2_set - body4_set - body5_set,
               '0001': body5_set - body1_set - body2_set - body3_set - body4_set,
               '1101': body1_set & body2_set & body3_set & body5_set - body4_set,
               '1011': body1_set & body2_set & body4_set & body5_set - body3_set,
               '0111': body2_set & body3_set & body4_set & body5_set - body1_set,
               '1110': body1_set & body3_set & body4_set & body5_set - body2_set,
               '1111': body1_set & body2_set & body3_set & body4_set & body5_set}

venn_diagram = venn3(subsets=(len(body1_set), len(body2_set), len(body1_set & body2_set),
               len(body3_set), len(body1_set & body3_set), len(body2_set & body3_set),
               len(body1_set & body2_set & body3_set)),
      set_labels=('Head', 'Prostate', 'Brain'))

for label in venn_diagram.set_labels: #type: ignore
    label.set_fontsize(8)

for subset in venn_diagram.subset_labels: 
    subset.set_fontsize(8)           #type: ignore

plt.title("Comparing Sequences Amongst Generated Customer Data")
plt.show()
