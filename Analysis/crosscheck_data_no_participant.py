import pandas as pd
import csv
##method using pandas
sample_set_crosscheck = pd.read_csv('sample_data.csv', sep=',')
#print(sample_set_crosscheck)
final = []
for id_1 in sample_set_crosscheck["entity:sample_id"]:
    for id_2 in sample_set_crosscheck["entity:sample_id"]:
        pair_name = id_1 + '_vs_' + id_2
        if id_1 != id_2:
            final.append([pair_name,
                         id_1,
                         id_2])           
#print(final)

crosscheck_data_no_participant = pd.DataFrame(final, columns = ['entity:pair_id', 'case_sample', 'control_sample'])
#print(crosscheck_data)

##download file
crosscheck_data_no_participant.to_csv('crosscheck_data_no_participant.tsv', index=False, sep = '\t')