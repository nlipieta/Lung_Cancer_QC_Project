import pandas as pd
import csv
##method using pandas
sample_set_crosscheck = pd.read_csv('sample_data.csv', sep=',')
#print(sample_set_crosscheck)
final = []
ids = set()
for id_1 in sample_set_crosscheck["entity:sample_id"]:
    for id_2 in sample_set_crosscheck["entity:sample_id"]:
        ids.add(tuple(sorted([id_1, id_2])))

for id_1, id_2 in ids:
    pair_name = id_1 + '_vs_' + id_2
    if id_1 != id_2 and not id_1.endswith('_RNAseq') and not id_2.endswith('_RNAseq'):
        final.append([pair_name,
                    id_1,
                    id_2,
                    'Crosscheck'])

crosscheck_data = pd.DataFrame(final, columns = ['entity:pair_id', 'case_sample', 'control_sample', 'participant'])
#print(crosscheck_data)

##download file
crosscheck_data.to_csv('crosscheck_data.tsv', index=False, sep = '\t')