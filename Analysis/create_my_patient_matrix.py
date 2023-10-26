import sys
import os.path
import subprocess
from io import StringIO

import numpy as np
import pandas as pd
import dalmatian
import matplotlib.pyplot as plt
import networkx as nx

files = subprocess.check_output("ls -1 per_patient_crosscheck/*metrics.tsv", shell = True)
files = files.decode("UTF-8").rstrip().split('\n')
participants = pd.read_csv('new_new_participant.tsv', sep = '\t')
dictionary = {}
tuples = set()
for x in files:
    expected_match_count = 0
    inconclusive_count = 0
    unexpected_mismatch_count = 0
    df = pd.read_csv(x, sep = '\t')
#    df_counts = df.RESULT.value_counts()
    for left in df.LEFT_GROUP_VALUE:
        for right in df.RIGHT_GROUP_VALUE:
            if left != right:
                tuples.add(tuple(sorted([left, right])))
    for i in list(range(len(df))):
        if (df.LEFT_GROUP_VALUE[i], df.RIGHT_GROUP_VALUE[i]) in tuples:
            if df.RESULT[i] == 'EXPECTED_MATCH':
                expected_match_count += 1
            if df.RESULT[i] == 'INCONCLUSIVE':
                inconclusive_count += 1
            if df.RESULT[i] == 'UNEXPECTED_MISMATCH':
                unexpected_mismatch_count += 1
    for i in participants.values:
        for y in i:
            if y in x:
                dictionary[y] = []
                dictionary[y].append(expected_match_count)
                dictionary[y].append(inconclusive_count)
                dictionary[y].append(unexpected_mismatch_count)
dataframe = pd.DataFrame(dictionary).T.reset_index()
dataframe.columns = ['patients', 'EXPECTED_MATCH', 'INCONCLUSIVE', 'UNEXPECTED_MISMATCH']
dataframe.to_csv('updated_flag_table.tsv', sep = '\t', index = False)