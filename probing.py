import pandas as pd

features_file = '/project/ssverma_shared/projects/Endometriosis/Endo_RuleBased_Phenotyping/symptom_pulls/Pheno/PMBB_2.3_pheno_covars.csv'
chart_labels_file = '/project/ssverma_shared/projects/Endometriosis/Endo_RuleBased_Phenotyping/chart_review_and_EHR_labels.csv'

features = pd.read_csv(features_file, sep=',')
labels = pd.read_csv(chart_labels_file, sep=',')

# endo = labels[labels['Chart_Adeno_or_Endo'] == '0.0']
# print(len(endo))

# print(labels['Chart_Adeno_or_Endo'].unique())

# for index, row in features.iterrows():
#     if features['endometriosis'] == 1:
#         print(features.loc[index])
# print(features.columns)
# print(labels.columns)

# label_comparisons = features.join(labels, on='PMBB_ID')
label_comparisons = labels.set_index('PMBB_ID').join(features.set_index('PMBB_ID'))
# label_comparisons = label_comparisons[['Chart_Adeno_or_Endo', 'endometriosis']]
# PMBB_ID, ICD_ENDO, Chart_Adeno_or_Endo
print(label_comparisons.columns) # -> pmbb ids and chart reviewed numbers indicating case (1.0) or control (0.0), and ICD_endo (1 indicates they think yes, 0 indicates they think no)

# TESTROWS = 5
# label_comparisons = label_comparisons[:TESTROWS]
total_cases = 1480
case_counter, total_case_counter = 0, 0
control_counter, total_control_counter = 0, 0
for index, row in label_comparisons.iterrows():
    if row['Chart_Adeno_or_Endo'] == 1:
        total_case_counter += 1
        if row['endometriosis'] == 1:
            case_counter += 1
    elif row['Chart_Adeno_or_Endo'] == 0:
        total_control_counter += 1
        if row['endometriosis'] == 0:
            control_counter += 1
# # get cases that are matching across features_file and chart_labels_file

print(case_counter) # 11% are misclassified in PMBB when comparing Endo ICDs to Endo Chart reviews. want to improve on this accuracy level to try and decrease what is misclassified
print(control_counter)
print(total_case_counter)
print(total_control_counter)
# always comparing to the chart reviews

            # (patient_endo_symptoms (abdominal_pelvic_pain ~yes))  
            # (patient_endo_symptoms (dysmenorrhea ~yes))   
            # (patient_endo_symptoms (pain_with_sex ~yes)) 
            # (patient_endo_symptoms (dyschezia ~yes)) 
            # (patient_endo_symptoms (dysuria ~yes)) 
            # (patient_endo_symptoms (infertility ~yes))   
            # (patient_endo_symptoms (pelvic_perineal_pain ~yes))
            # (patient_endo_symptoms (adenomyosis ~yes))

new_testing_data = label_comparisons.to_csv('/project/ssverma_shared/projects/Endometriosis/Endo_RuleBased_Phenotyping/new_features_covars.csv')

probe = label_comparisons[['Chart_Adeno_or_Endo', 'adenomyosis', 'dysmenorrhea', 'dyschezia', 'dysuria', 'pain_with_sex', 'infertility', 'abdominal_pelvic_pain', 'pelvic_perineal_pain']]
probes = probe.to_csv('/project/ssverma_shared/projects/Endometriosis/Endo_RuleBased_Phenotyping/relevant_features.csv')