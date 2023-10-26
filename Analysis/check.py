import pandas as pd

participant_flags = pd.read_csv('participant.flags.tsv', sep = '\t')
print(participant_flags)

#if (participant_flags.patient[participant_flags[participant_flags['UNEXPECTED_MISMATCH'] != 0].index[0]]):
#    print(participant_flags.patient)
unexp_mat = []

for x in participant_flags['patient']:
    if (participant_flags.UNEXPECTED_MISMATCH[participant_flags[participant_flags['patient'] == x].index[0]]) != 0:
        unexp_mat.append(x)
        
print(unexp_mat)