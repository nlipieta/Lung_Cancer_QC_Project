import pandas as pd
import csv

###with participant labels##
###method using pandas
#sample_set_qc = pd.read_csv('sample.tsv', sep='\t')
##print(sample_set_qc)
#tags = ['ICE', 'AGILENT', 'TWIST', 'RNAseq', 'WGS']
#final = []
#for id in sample_set_qc["entity:sample_id"]:
#    for tag in tags:
#        new_name = id + '_' + tag
#        if tag == 'ICE' and (sample_set_qc.ICE_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]) == (sample_set_qc.ICE_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]):
#            final.append([new_name,
#                          sample_set_qc.ICE_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
#                          sample_set_qc.ICE_crai_or_bai_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
#                          sample_set_qc.participant[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]])
#        if tag == 'AGILENT' and (sample_set_qc.AGILENT_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]) == (sample_set_qc.AGILENT_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]):
#            final.append([new_name,
#                          sample_set_qc.AGILENT_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
#                          sample_set_qc.AGILENT_crai_or_bai_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
#                          sample_set_qc.participant[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]])
#        if tag == 'TWIST' and (sample_set_qc.TWIST_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]) == (sample_set_qc.TWIST_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]):
#            final.append([new_name,
#                          sample_set_qc.TWIST_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
#                          sample_set_qc.TWIST_crai_or_bai_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
#                          sample_set_qc.participant[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]])
#        if tag == 'RNAseq' and (sample_set_qc.RNAseq_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]) == (sample_set_qc.RNAseq_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]):
#            final.append([new_name,
#                          sample_set_qc.RNAseq_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
#                          sample_set_qc.RNAseq_crai_or_bai_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
#                          sample_set_qc.participant[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]])
#        if tag == 'WGS' and (sample_set_qc.WGS_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]) == (sample_set_qc.WGS_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]):
#            final.append([new_name,
#                          sample_set_qc.WGS_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
#                          sample_set_qc.WGS_crai_or_bai_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
#                          sample_set_qc.participant[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]])
#sample_data = pd.DataFrame(final, columns = ['entity:sample_id', 'bam', 'bam_index', 'participant'])
##print(sample_data)

###download file
#sample_data.to_csv('sample_data.tsv', index=False, sep = '\t')

##with participant labels as 'Crosscheck'##
##method using pandas

sample_set_qc = pd.read_csv('sample.tsv', sep='\t')
print(sample_set_qc)
tags = ['ICE', 'AGILENT', 'TWIST', 'RNAseq', 'WGS']
final = []
ICE_count = 0
AGILENT_count = 0
TWIST_count = 0
RNAseq_count = 0
WGS_count = 0
sample_set_table = []
for id in sample_set_qc["entity:sample_id"]:
    for tag in tags:
        new_name = id + '_' + tag
        if tag == 'ICE' and (sample_set_qc.ICE_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]) == (sample_set_qc.ICE_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]):
            final.append([new_name,
                          sample_set_qc.ICE_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
                          sample_set_qc.ICE_crai_or_bai_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
                          'Crosscheck'])
            ICE_count += 1
        if tag == 'AGILENT' and (sample_set_qc.AGILENT_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]) == (sample_set_qc.AGILENT_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]):
            final.append([new_name,
                          sample_set_qc.AGILENT_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
                          sample_set_qc.AGILENT_crai_or_bai_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
                          'Crosscheck'])
            AGILENT_count += 1
        if tag == 'TWIST' and (sample_set_qc.TWIST_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]) == (sample_set_qc.TWIST_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]):
            final.append([new_name,
                          sample_set_qc.TWIST_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
                          sample_set_qc.TWIST_crai_or_bai_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
                          'Crosscheck'])
            TWIST_count += 1
        if tag == 'RNAseq' and (sample_set_qc.RNAseq_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]) == (sample_set_qc.RNAseq_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]):
            final.append([new_name,
                          sample_set_qc.RNAseq_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
                          sample_set_qc.RNAseq_crai_or_bai_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
                          'Crosscheck'])
            RNAseq_count += 1
        if tag == 'WGS' and (sample_set_qc.WGS_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]) == (sample_set_qc.WGS_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]]):
            final.append([new_name,
                          sample_set_qc.WGS_cram_or_bam_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
                          sample_set_qc.WGS_crai_or_bai_path[sample_set_qc[sample_set_qc['entity:sample_id']==id].index[0]],
                          'Crosscheck'])
            WGS_count += 1
            
for x in final:
    if x[0].endswith('_ICE'):
        sample_set_table.append([('ICE_' + str(ICE_count) + '_samples'), x[0]])
    if x[0].endswith('_AGILENT'):
        sample_set_table.append([('AGILENT_' + str(AGILENT_count) + '_samples'), x[0]])
    if x[0].endswith('_TWIST'):
        sample_set_table.append([('TWIST_' + str(TWIST_count) + '_samples'), x[0]])
    if x[0].endswith('_RNAseq'):
        sample_set_table.append([('RNAseq_' + str(RNAseq_count) + '_samples'), x[0]])
    if x[0].endswith('_WGS'):
        sample_set_table.append([('WGS_' + str(WGS_count) + '_samples'), x[0]])

#print(sample_set_table)
#sample_data_as_crosscheck = pd.DataFrame(final, columns = ['entity:sample_id', 'bam', 'bam_index', 'participant'])
#print(sample_data)

sample_set_table = pd.DataFrame(sample_set_table, columns = ['membership:sample_set_id', 'sample'])
##download file
#sample_data_as_crosscheck.to_csv('sample_data_as_crosscheck.tsv', index=False, sep = '\t')

sample_set_table.to_csv('sample_set_table.tsv', index=False, sep = '\t')