import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Your data
Turkey_Amira = set(["AALScout", "tse", "tse", "dess"])
Germany_VIDA = set(["AALScount", "tse", "tse", "tse", "tse", "tse", "tse"])
China_VIDA = set(["gre", "gre", "tse", "tse", "tse", "tse", "tse", "tse", "tse", "tse"])

# Create the Venn diagram
venn_labels = {'100': 'Turkey Amira', '010': 'Germany VIDA', '110': 'Common (Turkey Amira and Germany VIDA)',
               '001': 'China VIDA', '101': 'Common (Turkey Amira and China VIDA)', '011': 'Common (Germany VIDA and China VIDA)',
               '111': 'Common (Turkey Amira, Germany VIDA, and China VIDA)'}

def subset_label_formatter(x):
    try:
        return venn_labels[x]
    except KeyError:
        return ''

venn3(subsets=(len(Turkey_Amira), len(Germany_VIDA), len(Turkey_Amira.intersection(Germany_VIDA)),
               len(China_VIDA), len(Turkey_Amira.intersection(China_VIDA)), len(Germany_VIDA.intersection(China_VIDA)),
               len(Turkey_Amira.intersection(Germany_VIDA).intersection(China_VIDA))),
      set_labels=('Turkey Amira', 'Germany VIDA', 'China VIDA'), set_colors=('skyblue', 'lightgreen', 'lightcoral'),
      alpha=0.7, ax=plt.gca(), subset_label_formatter=subset_label_formatter)

# Title
plt.title('Venn Diagram of Sequences across 3 Countries for Knee Measurements')

# Show the plot
plt.show()
