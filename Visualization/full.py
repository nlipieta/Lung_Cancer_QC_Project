import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import greedy_modularity_communities
import seaborn as sns
#reference = pd.read_csv('Crosscheck_361_samples.matrix_output.txt', sep = '\t', index_col = 0)
reference = pd.read_csv('full_frame.tsv', sep = '\t', index_col = 0)

category = pd.read_csv('match_vs_sample_reference.tsv', sep = '\t')

colors = {'complete match':"red", "partial mismatch":"green", "complete mismatch":"blue"}

G = nx.Graph()

tuples = set()
    
for left in reference.columns.values:
    for right in reference.index.values:
        if reference[left][right] > 0:
            tuples.add(tuple(([left, right])))

new = set()

for x, y in tuples:
    new.add(x)
    new.add(y)
            
for x, y in tuples:
    G.add_node(x, color=colors[category['match status'][category[category['sample'] == x].index[0]]])
    G.add_node(y, color=colors[category['match status'][category[category['sample'] == y].index[0]]])
    if x != y:
        G.add_edge(x, y)
col = [node[1]['color'] for node in G.nodes(data=True)]
nx.draw(G, pos=nx.spring_layout(G), node_color=col, with_labels=True, font_weight='bold', font_size=6)
plt.savefig("full_network_graph_with_labels.pdf", bbox_inches="tight")
plt.show()

frame = pd.DataFrame(index = sorted(new), columns = sorted(new), dtype=float)
for x in new:
    for y in new:
        frame.loc[x, y] = max(float(reference.loc[x, y]), -109.9105)
fig, ax = plt.subplots(figsize=(32, 24))
sns.heatmap(frame, cmap="seismic", center=0)
columns = list(frame.columns.values)
index = list(frame.index.values)
ax.set_xticks(range(len(columns)))
ax.set_yticks(range(len(index)))
ax.set_xticklabels(columns, fontsize = 2)
ax.set_yticklabels(index, fontsize = 2)
plt.savefig("full_graph.pdf", bbox_inches="tight", dpi=600)
plt.show()