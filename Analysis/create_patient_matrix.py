import sys
import os.path
import subprocess
from io import StringIO

import numpy as np
import pandas as pd
import dalmatian


def read_crosscheck_metrics(gs_url):
    gsutil_command = ['gsutil', 'cat', gs_url]
    try:
        content = subprocess.check_output(gsutil_command, universal_newlines=True)
        lines = content.strip().split('\n')
        data_lines = [line for line in lines if not line.startswith('#')]
        return pd.read_csv(StringIO('\n'.join(data_lines)), sep='\t')
    except subprocess.CalledProcessError as e:
        print(f"Error downloading file from URL '{gs_url}': {e}")
        return None

# load workspace data via dalmatian
workspace = "broad-getzlab-awg-awad-lung-t/Heist_Hata_Lin_Lung_Cancer_QC_SampleSwap"
wm = dalmatian.WorkspaceManager(workspace)

# load pair table from Terra
pair_df = wm.get_pairs()
pair_df.loc[~pair_df.index.str.endswith("_pair")].to_csv("crosscheck_pair_runs.tsv", sep="\t")

# load sample table from Terra
sample_df = wm.get_samples()

columns = ["LEFT_GROUP_VALUE", "RIGHT_GROUP_VALUE", "RESULT", "LOD_SCORE"]

patient_flags = []

for participant, x in pair_df.groupby("participant"):
    pat_metrics = pd.read_csv(participant+".metrics.tsv", sep="\t")
#    df_participant = []
    expected_match_count = 0
    expected_mismatch_count = 0
    unexpected_match_count = 0
    unexpected_mismatch_count = 0
    inconclusive_count = 0
    print("participant: "+participant)
    
#    for _, row in x.iterrows():
#        df = read_crosscheck_metrics(row["crosscheck_metrics"])
#        metrics_paths = list(set(list(df["LEFT_FILE"])+list(df["RIGHT_FILE"])))
#        gs_paths = ["gs://"+path.replace("file:///cromwell_root/","") for path in metrics_paths]
#        sample_ids = [list(sample_df[sample_df["bam"]==gs_path].index)[0] for gs_path in gs_paths]

        # create dictionary that maps to sample IDs
#        sample_map = dict(zip(metrics_paths, sample_ids))
#        df["LEFT_GROUP_VALUE"] = df["LEFT_FILE"].map(sample_map)
#        df["RIGHT_GROUP_VALUE"] = df["RIGHT_FILE"].map(sample_map)
#        df_participant.append(df[columns])
        
    #results = [for result in pat_metrics]
    for result in pat_metrics['RESULT']:
        if result != "RESULT":
            if result == "EXPECTED_MATCH":
                expected_match_count += 1
            if result == "UNEXPECTED_MATCH":
                unexpected_match_count += 1
            if result == "EXPECTED_MISMATCH":
                expected_mismatch_count += 1
            if result == "UNEXPECTED_MISMATCH":
                unexpected_mismatch_count += 1
            if result == "INCONCLUSIVE":
                inconclusive_count += 1
                
    patient_flags.append([participant, expected_match_count, unexpected_match_count, expected_mismatch_count, unexpected_mismatch_count])
            
    # save per-participant metrics file
#    pd.concat(df_participant).to_csv(participant+".metrics.tsv", index=False, sep="\t")
patient_flags = pd.DataFrame(patient_flags, columns = ["patient", "EXPECTED_MATCH", "UNEXPECTED_MATCH", "EXPECTED_MISMATCH", "UNEXPECTED_MISMATCH"])
(patient_flags).to_csv("participant.flags.tsv", index = False, sep = '\t')