import matplotlib.pyplot as plt
from matplotlib_venn import venn5 # type: ignore

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

venn_labels = {'10000': body1_set - body2_set - body3_set - body4_set - body5_set,
               '01000': body2_set - body1_set - body3_set - body4_set - body5_set,
               '00100': body3_set - body1_set - body2_set - body4_set - body5_set,
               '00010': body4_set - body1_set - body2_set - body3_set - body5_set,
               '00001': body5_set - body1_set - body2_set - body3_set - body4_set,
               '11000': body1_set & body2_set - body3_set - body4_set - body5_set,
               '10100': body1_set & body3_set - body2_set - body4_set - body5_set,
               '10010': body1_set & body4_set - body2_set - body3_set - body5_set,
               '10001': body1_set & body5_set - body2_set - body3_set - body4_set,
               '01100': body2_set & body3_set - body1_set - body4_set - body5_set,
               '01010': body2_set & body4_set - body1_set - body3_set - body5_set,
               '01001': body2_set & body5_set - body1_set - body3_set - body4_set,
               '00110': body3_set & body4_set - body1_set - body2_set - body5_set,
               '00101': body3_set & body5_set - body1_set - body2_set - body4_set,
               '00011': body4_set & body5_set - body1_set - body2_set - body3_set,
               '11100': body1_set & body2_set & body3_set - body4_set - body5_set,
               '11010': body1_set & body2_set & body4_set - body3_set - body5_set,
               '11001': body1_set & body2_set & body5_set - body3_set - body4_set,
               '10110': body1_set & body3_set & body4_set - body2_set - body5_set,
               '10101': body1_set & body3_set & body5_set - body2_set - body4_set,
               '10011': body1_set & body4_set & body5_set - body2_set - body3_set,
               '01110': body2_set & body3_set & body4_set - body1_set - body5_set,
               '01101': body2_set & body3_set & body5_set - body1_set - body4_set,
               '01011': body2_set & body4_set & body5_set - body1_set - body3_set,
               '00111': body3_set & body4_set & body5_set - body1_set - body2_set,
               '11110': body1_set & body2_set & body3_set & body4_set - body5_set,
               '11101': body1_set & body2_set & body4_set & body5_set - body3_set,
               '11011': body1_set & body3_set & body4_set & body5_set - body2_set,
               '10111': body2_set & body3_set & body4_set & body5_set - body1_set,
               '01111': body2_set & body3_set & body4_set & body5_set - body1_set,
               '11111': body1_set & body2_set & body3_set & body4_set & body5_set}

venn_diagram = venn5(subsets=(len(body1_set), len(body2_set), len(body1_set & body2_set),
                              len(body3_set), len(body1_set & body3_set), len(body2_set & body3_set),
                              len(body1_set & body2_set & body3_set),
                              len(body4_set), len(body1_set & body4_set), len(body2_set & body4_set),
                              len(body1_set & body2_set & body4_set), len(body3_set & body4_set),
                              len(body1_set & body3_set & body4_set), len(body2_set & body3_set & body4_set),
                              len(body1_set & body2_set & body3_set & body4_set),
                              len(body5_set), len(body1_set & body5_set), len(body2_set & body5_set),
                              len(body1_set & body2_set & body5_set), len(body3_set & body5_set),
                              len(body1_set & body3_set & body5_set), len(body2_set & body3_set & body5_set),
                              len(body1_set & body2_set & body3_set & body5_set),
                              len(body4_set & body5_set), len(body1_set & body4_set & body5_set),
                              len(body2_set & body4_set & body5_set), len(body1_set & body2_set & body4_set & body5_set),
                              len(body3_set & body4_set & body5_set), len(body1_set & body3_set & body4_set & body5_set),
                              len(body2_set & body3_set & body4_set & body5_set),
                              len(body1_set & body2_set & body3_set & body4_set & body5_set)),
                     set_labels=('Body 1', 'Body 2', 'Body 3', 'Body 4', 'Body 5'))

for label in venn_diagram.set_labels:
    label.set_fontsize(8)

for subset in venn_diagram.subset_labels:
    subset.set_fontsize(8)

plt.title("Comparing Sequences Amongst Generated Customer Data")
plt.show()
