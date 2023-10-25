import pandas as pd
import matplotlib.pyplot as plt

dict = {}
list_x = []

pairs = pd.read_csv("final_participant_reference.tsv", sep = '\t')

for patient in pairs['participant']:
    dict[patient] = [0, 0, 0, 0, 0]

for sample in pairs["entity:sample_id"]:
    if sample.endswith("ICE"):
        dict[((pairs["participant"])[pairs[pairs["entity:sample_id"]==sample].index[0]])][0] += 1
    if sample.endswith("TWIST"):
        dict[((pairs["participant"])[pairs[pairs["entity:sample_id"]==sample].index[0]])][1] += 1
    if sample.endswith("AGILENT"):
        dict[((pairs["participant"])[pairs[pairs["entity:sample_id"]==sample].index[0]])][2] += 1
    if sample.endswith("RNAseq"):
        dict[((pairs["participant"])[pairs[pairs["entity:sample_id"]==sample].index[0]])][3] += 1
    if sample.endswith("WGS"):
        dict[((pairs["participant"])[pairs[pairs["entity:sample_id"]==sample].index[0]])][4] += 1

for key, value in dict.items():
    ini = [key]
    for x in value:
        ini.append(x)
    list_x.append(ini)

bar_df = pd.DataFrame(list_x, columns = ["patient", "ICE", "TWIST", "AGILENT", "RNAseq", "WGS"])
bar_df.to_csv("bar_df.tsv", sep = '\t', index = False)

bar_df.plot(x='patient', kind='bar', stacked=True,
        title='Sample Type Barplot', cmap = 'turbo')
plt.show()
plt.savefig("bar_plot.png", dpi = 300)