import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Your data
knee_175608 = set(["gre", "gre", "tse", "tse", "tse", "tse", "tse", "tse"])
knee_182627 = set(["AALScout", "tse", "tse_dixon", "tse_dixon", "tse", "fl3d_vibe", "tse_dixon", "fl3d_vibe", "haste"])
knee_202531 = set(["AALScout", "tse", "space", "tse", "tse", "tse", "tse"])

# Create the Venn diagram
venn_labels = {'100': 'Knee 175608', '010': 'Knee 182627', '110': 'Common (Knee 175608 and Knee 182627)',
               '001': 'Knee 202531', '101': 'Common (Knee 175608 and Knee 202531)', '011': 'Common (Knee 182627 and Knee 202531)',
               '111': 'Common (Knee 175608, Knee 182627, and Knee 202531)'}

def subset_label_formatter(x):
    try:
        return venn_labels[x]
    except KeyError:
        return ''

venn3(subsets=(len(knee_175608), len(knee_182627), len(knee_175608.intersection(knee_182627)),
               len(knee_202531), len(knee_175608.intersection(knee_202531)), len(knee_182627.intersection(knee_202531)),
               len(knee_175608.intersection(knee_182627).intersection(knee_202531))),
      set_labels=('Knee 175608\n' + str(len(knee_175608)), 'Knee 182627\n' + str(len(knee_182627)), 'Knee 202531\n' + str(len(knee_202531))),
      set_colors=('skyblue', 'lightgreen', 'lightcoral'),
      alpha=0.7, ax=plt.gca(), subset_label_formatter=subset_label_formatter)

# Title
plt.title('Venn Diagram of Knee Sequences across 3 Customers')

# Show the plot
plt.show()
