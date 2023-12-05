import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import greedy_modularity_communities
import seaborn as sns
#reference = pd.read_csv('Crosscheck_361_samples.matrix_output.txt', sep = '\t', index_col = 0)
reference = pd.read_csv('full_frame.tsv', sep = '\t', index_col = 0)

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
    G.add_node(x)
    G.add_node(y)
    if x != y:
        G.add_edge(x, y)

c = list(greedy_modularity_communities(G))

data = []

for set in c:
    if len(set) < 2:
        for sample in set:
            data.append([sample])
            
data = pd.DataFrame(data, columns = ['samples'])
data.to_csv('complete_mismatch_samples.tsv', sep = '\t', index = False)