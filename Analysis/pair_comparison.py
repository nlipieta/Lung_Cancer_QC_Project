import pandas as pd

reference = pd.read_csv('edge_count_match_categorization.tsv', sep = '\t')

dictionary = {}
patient_vs_sample = {}
tuples = set()
lists = []

for idx, category in reference['match status'].items():
    if category == 'complete match':
        patient_vs_sample[reference['patient'][idx]] = reference['sample'][idx]

for idx, category in reference['match status'].items():
    if category == 'partial mismatch' or category == 'complete mismatch':
        if reference['patient'][idx] in patient_vs_sample.keys():
            if patient_vs_sample[reference['patient'][idx]] not in dictionary:
                dictionary[patient_vs_sample[reference['patient'][idx]]] = []
            else:
                dictionary[patient_vs_sample[reference['patient'][idx]]].append(reference['sample'][idx])
        
for key, value in dictionary.items():
    for x in value:
        tuples.add(tuple(([key, x])))
        
for x, y in tuples:
    lists.append([x + '_vs_' + y, x, y, reference['patient'][reference[reference['sample'] == x].index[0]]])

lists = pd.DataFrame(lists)
lists.columns = ['entity:pair_id', 'normal', 'compare', 'patient']
lists = lists.sort_values(by = 'patient')
lists.to_csv('pair_comparison.tsv', sep = '\t', index = False)