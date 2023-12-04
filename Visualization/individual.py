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
            
for x, y in tuples:
    if x != y:
        G.add_node(x)
        G.add_node(y)
        G.add_edge(x, y)
        
dictionary = {}
count = 0
c = list(greedy_modularity_communities(G))
for i in c:
    dictionary[count] = []
    for x in i:
        dictionary[count].append(x)
    count += 1
print(dictionary)
        
###make individual heatmaps
for id, value in dictionary.items():
    frame = pd.DataFrame(index=list(value), columns=list(value), dtype=float)
    for left in value:
        for right in value:
            
###coded
#            if reference[left][right] < 0:
#                frame.loc[left, right] = 1
#            elif reference[left][right] == 0:
#                frame.loc[left, right] = 2
#            elif left.startswith((right.split("_")[0]).split('-')[0]):
#                frame.loc[left, right] = 3
#            elif not left.startswith((right.split("_")[0]).split('-')[0]):
#                frame.loc[left, right] = 4
#
#    cmap = sns.color_palette(["blue", "white", "red", "orange"])
#
#    sns.heatmap(frame, cmap=cmap, vmax = 4, vmin = 1)
#    plt.savefig(str(id) + "_graph_coded.pdf", bbox_inches="tight")
#    plt.show()

###non-coded
            frame.loc[left, right] = float(reference[left][right])
    sns.heatmap(frame, cmap="seismic", center=0)
    plt.savefig(str(id) + "_graph.pdf", bbox_inches="tight")
    plt.show()

#make individual network graphs
for id, value in dictionary.items():
    G = nx.Graph()
    for y in value:
        for x in value:
            frame.loc[x, y] = float(reference[x][y])
            G.add_node(x, color=colors[category['match status'][category[category['sample'] == x].index[0]]])
            G.add_node(y, color=colors[category['match status'][category[category['sample'] == y].index[0]]])
            if ((x, y) in tuples or (y, x) in tuples) and x != y:
                G.add_edge(x, y)     
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.savefig(str(id) + "_network_graph.pdf", bbox_inches="tight")
    plt.show()