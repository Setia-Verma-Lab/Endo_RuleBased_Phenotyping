import pandas as pd

features_file = '/project/ssverma_shared/projects/Endometriosis/Endo_RuleBased_Phenotyping/symptom_pulls/Pheno/PMBB_2.3_pheno_covars.csv'
chart_labels_file = '/project/ssverma_shared/projects/Endometriosis/Endo_RuleBased_Phenotyping/chart_review_and_EHR_labels.csv'

features = pd.read_csv(features_file, sep=',', index_col='PMBB_ID')
labels = pd.read_csv(chart_labels_file, sep=',', index_col='PMBB_ID')

for index, row in features.iterrows():
    if features['endometriosis'] == 1:
        print(features.loc[index])

label_comparisons = features.join(labels.set_index('PMBB_ID'), on='PMBB_ID')
label_comparisons = label_comparisons[['PMBB_ID', 'Chart_Adeno_or_Endo']]
# PMBB_ID, ICD_ENDO, Chart_Adeno_or_Endo

# get cases that are matching across features_file and chart_labels_file
