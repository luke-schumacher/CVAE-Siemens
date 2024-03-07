import pandas as pd

# Read the initial data from a CSV file
csv_file_path = 'encoded_data/Knee/flawless_seq.csv'  # Replace with your actual file path
df = pd.read_csv(csv_file_path)

# Your desired sequences organized for readability
desired_sequences = """Seq_AALScout, Seq_BEAT, Seq_BEAT_epi, Seq_BEAT_FQ, Seq_BEAT_FQ_nav, Seq_BEAT_interactive,
Seq_BEAT_map, Seq_blade, Seq_bs_calibration, Seq_ciss, Seq_csi_se, Seq_csi_slaser, Seq_CV_nav, Seq_dess,
Seq_ep_seg_fid, Seq_ep2d_asl, Seq_ep2d_bold, Seq_ep2d_diff, Seq_ep2d_fid, Seq_ep2d_pace, Seq_ep2d_se,
Seq_ep2d_se_mre, Seq_ep2d_se_ms, Seq_fast_tse, Seq_fid, Seq_fl_pc, Seq_fl_peri_tof, Seq_fl3d_ce,
Seq_fl3d_rd, Seq_fl3d_vibe, Seq_gre, Seq_gre_b0map, Seq_gre_field_mapping, Seq_gre_phs, Seq_gre_proj,
Seq_gre_wave, Seq_greMRE, Seq_haste, Seq_haste_diff, Seq_medic, Seq_MRF, Seq_petra, Seq_psif, Seq_qDWI,
Seq_resolve, Seq_se, Seq_se_15b130, Seq_se_17rb130, Seq_se_mc, Seq_semac, Seq_space, Seq_space_nav,
Seq_svs_se, Seq_svs_st, Seq_svs_st_histo, Seq_tfl, Seq_tfl_b1map, Seq_tfl_cb, Seq_tgse, Seq_tgse_asl,
Seq_trufi, Seq_trufi_freqScout, Seq_tse, Seq_tse_dixon, Seq_tse_MDME, Seq_twist"""

# Convert the desired sequences to a list
desired_sequences_list = [sequence.strip() for sequence in desired_sequences.strip().split(',')]

# Identify missing sequences
missing_sequences = set(desired_sequences_list) - set(df.columns)

# Add missing sequences as new columns with corresponding columns filled with 0s
for sequence in missing_sequences:
    df[sequence] = 0

# Reorder columns alphabetically
df = df[sorted(df.columns)]

# Save the final DataFrame as a CSV file
output_csv_path = 'encoded_data/Knee/unified_seq_202531_knee.csv'  # Replace with your desired output file path
df.to_csv(output_csv_path, index=False)

# Print the final DataFrame
print(df)
print(f"\nFinal DataFrame saved to: {output_csv_path}")
