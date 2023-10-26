import sys
import os.path
import subprocess
from io import StringIO

import numpy as np
import pandas as pd
import dalmatian
import matplotlib.pyplot as plt
import networkx as nx

match_vs_tags = {"ICE" : [0, 0, 0],
                 'TWIST': [0, 0, 0],
                 'AGILENT': [0, 0, 0],
                 'RNAseq': [0, 0, 0],
                 'WGS': [0, 0, 0]}
final_list = []
samples = {}
reference = pd.read_csv('final_participant_reference.tsv', sep = '\t')
for x in reference['entity:sample_id']:
    if reference.participant[reference[reference['entity:sample_id'] == x].index[0]] not in samples:
        samples[reference.participant[reference[reference['entity:sample_id'] == x].index[0]]] = 1
    else:
        samples[reference.participant[reference[reference['entity:sample_id'] == x].index[0]]] += 1
files = subprocess.check_output("ls -1 per_patient_crosscheck/*metrics.tsv", shell = True)
files = files.decode("UTF-8").rstrip().split('\n')
dictionary = {}
tuples = set()
for x in files:
    match_category = str()
    prefix = os.path.basename(x).split("_crosscheck_")[0]
    df = pd.read_csv(x, sep = '\t')
    for left in df.LEFT_GROUP_VALUE:
        for right in df.RIGHT_GROUP_VALUE:
            if left != right:
                tuples.add(tuple(sorted([left, right])))
    edge_count = {}
    for x, y in tuples:
        edge_count[x] = 0
        edge_count[y] = 0
    total_count = 0
    for i in list(range(len(df))):
        if (df.LEFT_GROUP_VALUE[i], df.RIGHT_GROUP_VALUE[i]) in tuples:
            if df.RESULT[i] == 'EXPECTED_MATCH':
                edge_count[df.LEFT_GROUP_VALUE[i]] += 1
                edge_count[df.RIGHT_GROUP_VALUE[i]] += 1
                total_count += 1
            else:
                total_count += 1
        patient_name = os.path.basename(prefix).split(".")[0]
    for key, value in edge_count.items():
        if reference.participant[reference[reference['entity:sample_id'] == key].index[0]] == patient_name:
            if value == (samples[patient_name]-1):
                match_category = 'complete match'
                if key.endswith('ICE'):
                    match_vs_tags['ICE'][0] += 1
                if key.endswith('TWIST'):
                    match_vs_tags['TWIST'][0] += 1
                if key.endswith('WGS'):
                    match_vs_tags['WGS'][0] += 1
                if key.endswith('RNAseq'):
                    match_vs_tags['RNAseq'][0] += 1
                if key.endswith('AGILENT'):
                    match_vs_tags['AGILENT'][0] += 1
            elif value > 0:
                match_category = 'partial mismatch'
                if key.endswith('ICE'):
                    match_vs_tags['ICE'][1] += 1
                if key.endswith('TWIST'):
                    match_vs_tags['TWIST'][1] += 1
                if key.endswith('WGS'):
                    match_vs_tags['WGS'][1] += 1
                if key.endswith('RNAseq'):
                    match_vs_tags['RNAseq'][1] += 1
                if key.endswith('AGILENT'):
                    match_vs_tags['AGILENT'][1] += 1
            elif value == 0:
                match_category = 'complete mismatch'
                if key.endswith('ICE'):
                    match_vs_tags['ICE'][2] += 1
                if key.endswith('TWIST'):
                    match_vs_tags['TWIST'][2] += 1
                if key.endswith('WGS'):
                    match_vs_tags['WGS'][2] += 1
                if key.endswith('RNAseq'):
                    match_vs_tags['RNAseq'][2] += 1
                if key.endswith('AGILENT'):
                    match_vs_tags['AGILENT'][2] += 1
            final_list.append([patient_name, key, value, samples[patient_name], match_category])
final_df = pd.DataFrame(final_list, columns = ['patient', 'sample', 'match', 'samples', 'match status'])
#final_df.to_csv('edge_count.tsv', sep = '\t', index = False)
final_df.to_csv('edge_count_match_categorization.tsv', sep = '\t', index = False)
match_vs_tags = pd.DataFrame(match_vs_tags).T.reset_index()
match_vs_tags.columns = ['tags', 'complete match', 'partial mismatch', 'complete mismatch']
match_vs_tags.to_csv('match_vs_tags.tsv', sep = '\t', index = False)