###import###
import pandas as pd
import numpy as np
import dalmatian
import pathlib

# for working with multiprocessing
import re
import os
import subprocess
from multiprocessing import Pool
from io import StringIO
from concurrent.futures import ThreadPoolExecutor

from IPython.display import display
from google.cloud import storage

# For plotting / visualization
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from plotly.offline import iplot
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

final_df = {}

namespace = "broad-getzlab-awg-awad-lung-t"
workspace = "Heist_Hata_Lin_Lung_Cancer_QC_SampleSwap"
full_workspace = namespace+"/"+workspace

wm = dalmatian.WorkspaceManager(full_workspace)

sample_df = wm.get_samples()

def download_gcs_file(gs_url):
    try:
        gsutil_command = ['gsutil', 'cat', gs_url]
        return subprocess.check_output(gsutil_command, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        print(f"Error downloading file from URL '{gs_url}': {e}")
        return None

def parse_gcs_content(content):
    if content is None:
        return None
    lines = content.strip().split('\n')
    data_lines = [line for line in lines if not line.startswith('#')] # skip all the headers
    return pd.read_csv(StringIO('\n'.join(data_lines)), sep='\t')

def get_crosscheck_metrics(df):
    for idx, crosscheck_metrics_url in df['hsMetrics'].items():
        if not pd.isna(crosscheck_metrics_url):
            content = download_gcs_file(crosscheck_metrics_url)
            fragment_df = parse_gcs_content(content)
            tag = str()
            mean_target_coverage = fragment_df['MEAN_TARGET_COVERAGE'][0]
            pct_target_bases_30x = fragment_df['PCT_TARGET_BASES_30X'][0]
            pct_target_bases_50x = fragment_df['PCT_TARGET_BASES_50X'][0]
            if idx.endswith('ICE'):
                tag = 'ICE'
            elif idx.endswith('TWIST'):
                tag = 'TWIST'
            elif idx.endswith('AGILENT'):
                tag = 'AGILENT'
            elif idx.endswith('WGS'):
                tag = 'WGS'
            final_df[idx] = [tag, mean_target_coverage, pct_target_bases_30x, pct_target_bases_50x]
            
(get_crosscheck_metrics(sample_df))
final_df = pd.DataFrame(final_df).T.reset_index()
final_df.columns = ['SAMPLE', 'BAIT_SET', 'MEAN_TARGET_COVERAGE', 'PCT_TARGET_BASES_30X', 'PCT_TARGET_BASES_50X']
final_df.to_csv('sample_hsMetrics_parse.tsv', sep = '\t', index = False)