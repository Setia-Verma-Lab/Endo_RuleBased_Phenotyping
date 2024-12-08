import clips
import pandas as pd
import sys
sys.path.append('./src/')
from clips_util import print_facts, print_rules, print_templates, build_read_assert

evaluation_dict = {'only_endo_predicted':0, 'only_endo_actual':0, 'only_concomitant_predicted':0, 'only_concomitant_actual':0, 'both_endo_concomitant_predicted':0, 'both_endo_concomitant_actual':0, 'neither_endo_concomitant_predicted':0, 'neither_endo_concomitant_actual':0}

def store_result(*args):
    endo, other = args
    # print(endo)
    # print(other)
    if endo == "endo_0" and other == "other_0":
        evaluation_dict['neither_endo_concomitant_predicted'] += 1
    elif endo == "endo_0" and other == "other_1":
        evaluation_dict['only_concomitant_predicted'] += 1
    elif endo == "endo_1" and other == "other_0":
        evaluation_dict['only_endo_predicted'] += 1
    elif endo == "endo_1" and other == "other_1":
        evaluation_dict['both_endo_concomitant_predicted'] += 1

# create the CLIPS environment
env = clips.Environment()

env.define_function(store_result)

DEFTEMPLATE_PATIENT_ENDOMETRIOSIS_SYMPTOMS = """
(deftemplate patient_endo_symptoms
    (slot abdominal_pelvic_pain (type SYMBOL)
        (allowed-symbols yes no unknown))
    (slot dysmenorrhea (type SYMBOL)
        (allowed-symbols yes no unknown))
    (slot pain_with_sex (type SYMBOL)
        (allowed-symbols yes no unknown))
    (slot dyschezia (type SYMBOL)
        (allowed-symbols yes no unknown))
    (slot dysuria (type SYMBOL)
        (allowed-symbols yes no unknown))
    (slot infertility (type SYMBOL)
        (allowed-symbols yes no unknown))
    (slot pelvic_perineal_pain (type SYMBOL)
        (allowed-symbols yes no unknown))

    )
"""
env.build(DEFTEMPLATE_PATIENT_ENDOMETRIOSIS_SYMPTOMS)

# patient concomitant disease symptoms
DEFTEMPLATE_PATIENT_CONCOMITANT_DISEASE_SYMPTOMS = """
(deftemplate patient_concomitant_disease_symptoms
    (slot amenorrhea (type SYMBOL) 
        (allowed-symbols yes no unknown))
    (slot constipation (type SYMBOL)
        (allowed-symbols yes no unknown))
    (slot diarrhea (type SYMBOL)
        (allowed-symbols yes no unknown))
    (slot flank_pain (type SYMBOL)
        (allowed-symbols yes no unknown))
    (slot hematuria (type SYMBOL)
        (allowed-symbols yes no unknown))
    (slot frequent_urination (type SYMBOL)
        (allowed-symbols yes no unknown))
    (slot adenomyosis (type SYMBOL)
        (allowed-symbols yes no unknown))

)
"""
env.build(DEFTEMPLATE_PATIENT_CONCOMITANT_DISEASE_SYMPTOMS)

# participant inclusion criteria met status
DEFTEMPLATE_ENDOMETRIOSIS_INCLUSION = """
(deftemplate endometriosis_inclusion
    (slot meets_criteria (type SYMBOL)
    (allowed-symbols yes no unknown))
)
"""
env.build(DEFTEMPLATE_ENDOMETRIOSIS_INCLUSION)

# participant trial eligibility status
DEFTEMPLATE_CONCOMITANT_DISEASE_INCLUSION = """
(deftemplate concomitant_disease_inclusion
    (slot meets_criteria (type SYMBOL)
    (allowed-symbols yes no unknown))
)
"""
env.build(DEFTEMPLATE_CONCOMITANT_DISEASE_INCLUSION)

# Add deffacts that the inclusion, exclusion, trial eligibility, and child bearing status are all unknown
DEFFCATS_INITIAL_STATUS = """
(deffacts starting_inclusion_exclusion_facts "Set the inclusion criteria met to unknown"
    (endometriosis_inclusion (meets_criteria unknown))
    (concomitant_disease_inclusion (meets_criteria unknown))
)
"""
env.build(DEFFCATS_INITIAL_STATUS)

# reset the environment to make sure the deffacts are added
# env.reset()

# ; RULE: Inclusion Criteria Are Not Met
# ; *Forward chaining to determine if participant is not eligible for study based on inclusion criteria facts
# ; INPUT: Criteria based on inclusion criteria defined in study. 
# ; OUTPUT: Trial eligibility No, Inclusion Criteria Met No
DEFRULE_ENDOMETRIOSIS_INCLUSION_CRITERIA_NOT_MET = """
(defrule endo-inclusion-criteria-not-met "Rule to define a person not having any symptoms consistent with endometriosis"
    (logical
        (and
            (patient_endo_symptoms (abdominal_pelvic_pain ~yes))  
            (patient_endo_symptoms (dysmenorrhea ~yes))   
            (patient_endo_symptoms (pain_with_sex ~yes)) 
            (patient_endo_symptoms (dyschezia ~yes)) 
            (patient_endo_symptoms (dysuria ~yes)) 
            (patient_endo_symptoms (infertility ~yes))   
            (patient_endo_symptoms (pelvic_perineal_pain ~yes))
        )
    )

    ?f1 <-(endometriosis_inclusion (meets_criteria unknown))

    => 

    (modify ?f1 (meets_criteria no))
)
"""
env.build(DEFRULE_ENDOMETRIOSIS_INCLUSION_CRITERIA_NOT_MET)

# indicates presence of symptom(s) that are consistent with endometriosis
DEFRULE_ENDOMETRIOSIS_INCLUSION_CRITERIA_MET = """
(defrule endo-inclusion-criteria-met "Rule to define a person as having symptom(s) consistent with endometriosis"
    (logical
        (or
            (patient_endo_symptoms (abdominal_pelvic_pain yes))  
            (patient_endo_symptoms (dysmenorrhea yes))   
            (patient_endo_symptoms (pain_with_sex yes)) 
            (patient_endo_symptoms (dyschezia yes)) 
            (patient_endo_symptoms (dysuria yes)) 
            (patient_endo_symptoms (infertility yes))   
            (patient_endo_symptoms (pelvic_perineal_pain yes))
        )
    )

    ?f1 <-(endometriosis_inclusion (meets_criteria unknown))

    => 

    (modify ?f1 (meets_criteria yes))
)
"""
env.build(DEFRULE_ENDOMETRIOSIS_INCLUSION_CRITERIA_MET)

# indicates presence of symptoms that indicate no concomitant disease (along with or instead of) endometriosis
DEFRULE_CONCOMITANT_DISEASE_INCLUSION_CRITERIA_NOT_MET = """
(defrule concomitant-inclusion-criteria-not-met "Rule to define a person as having symptom(s) not consistent with other (non-endo) disease based on inclusion criteria facts"
    (logical
        (and
            (patient_concomitant_disease_symptoms (amenorrhea ~yes))  
            (patient_concomitant_disease_symptoms (constipation ~yes))   
            (patient_concomitant_disease_symptoms (diarrhea ~yes)) 
            (patient_concomitant_disease_symptoms (flank_pain ~yes)) 
            (patient_concomitant_disease_symptoms (hematuria ~yes)) 
            (patient_concomitant_disease_symptoms (frequent_urination ~yes))   
            (patient_concomitant_disease_symptoms (adenomyosis ~yes))
        )
    )

    ?f1 <-(concomitant_disease_inclusion (meets_criteria unknown))

    => 

    (modify ?f1 (meets_criteria no))
)
"""
env.build(DEFRULE_CONCOMITANT_DISEASE_INCLUSION_CRITERIA_NOT_MET)

# indicates presence of symptoms that indicate concomitant disease (along with or instead of) endometriosis
DEFRULE_CONCOMITANT_DISEASE_INCLUSION_CRITERIA_MET = """
(defrule concomitant-inclusion-criteria-met "Rule to define a person as having symptom(s) consistent with other (non-endo) disease based on inclusion criteria facts"
    (logical
        (or
            (patient_concomitant_disease_symptoms (amenorrhea yes))  
            (patient_concomitant_disease_symptoms (constipation yes))   
            (patient_concomitant_disease_symptoms (diarrhea yes)) 
            (patient_concomitant_disease_symptoms (flank_pain yes)) 
            (patient_concomitant_disease_symptoms (hematuria yes)) 
            (patient_concomitant_disease_symptoms (frequent_urination yes))   
            (patient_concomitant_disease_symptoms (adenomyosis yes))
        )
    )

    ?f1 <-(concomitant_disease_inclusion (meets_criteria unknown))

    => 

    (modify ?f1 (meets_criteria yes))
)
"""
env.build(DEFRULE_CONCOMITANT_DISEASE_INCLUSION_CRITERIA_MET)
# not going to try and classify the concomitant disease - but will factor whether they do have a concomitant disease (IBS, or interstitial cystitis, or adenomyosis) in my evaluation
    # because I don't have detailed symptom data for all of the concomitant diseases, only some of them

DEFRULE_ENDOMETRIOSIS_AND_CONCOMITANT_INCLUSION = """
(defrule endo-and-concomitant-inclusion
    (endometriosis_inclusion (meets_criteria yes))
    (concomitant_disease_inclusion (meets_criteria yes))
    =>
    (println "___________")
    (println "Symptoms are consistent with both endometriosis and presence of concomitant disease. [recommendation]")
    (println "___________")
    (store_result "endo_1" "other_1")
)
"""
env.build(DEFRULE_ENDOMETRIOSIS_AND_CONCOMITANT_INCLUSION)

DEFRULE_ENDOMETRIOSIS_AND_CONCOMITANT_EXCLUSION = """
(defrule endo-and-concomitant-exclusion
    (endometriosis_inclusion (meets_criteria no))
    (concomitant_disease_inclusion (meets_criteria no))
    =>
    (println "___________")
    (println "Symptoms are consistent with neither endometriosis nor concomitant diseases that we screened for (IBS, adenomyosis, others). [recommendation]")
    (println "___________")
    (store_result "endo_0" "other_0")
)
"""
env.build(DEFRULE_ENDOMETRIOSIS_AND_CONCOMITANT_EXCLUSION)

DEFRULE_ONLY_ENDOMETRIOSIS_INCLUSION = """
(defrule only-endo-inclusion
    (endometriosis_inclusion (meets_criteria yes))
    (concomitant_disease_inclusion (meets_criteria no))
    =>
    (println "___________")
    (println "Patient has symptom(s) consistent only with endometriosis and not additional diseases")
    (println "___________")
    (store_result "endo_1" "other_0")
)
"""
env.build(DEFRULE_ONLY_ENDOMETRIOSIS_INCLUSION)

DEFRULE_ONLY_ENDOMETRIOSIS_EXCLUSION = """
(defrule only-endo-exclusion
    (endometriosis_inclusion (meets_criteria no))
    (concomitant_disease_inclusion (meets_criteria yes))
    =>
    (println "___________")
    (println "Patient has symptom(s) consistent only with non-endo diseases")
    (println "___________")
    (store_result "endo_0" "other_1")
)
"""
env.build(DEFRULE_ONLY_ENDOMETRIOSIS_EXCLUSION)

# three outputs
# calculate accuracy, PPV, NPV for each case

# and ablation analysis

data_file = '/project/ssverma_shared/projects/Endometriosis/Endo_RuleBased_Phenotyping/symptom_pulls/Pheno/PMBB_2.3_pheno_covars.csv'

data = pd.read_csv(data_file, sep=',', index_col='PMBB_ID')

# run each row at a time, then evaluate correctness and store in another object

# retrieve the fact templates
patient_endo_template = env.find_template('patient_endo_symptoms')
patient_concomitant_disease_template = env.find_template('patient_concomitant_disease_symptoms')

# # Find distinct values and their range
# NAME = 'infertility'
# distinct_values = data[NAME].unique()
# value_range = (distinct_values.min(), distinct_values.max())

# print(f"Distinct values in {NAME}: {sorted(distinct_values)}")
# print(f"Range of distinct values in {NAME}: {value_range}")

TESTROWS = 10
# data = data.iloc[:TESTROWS]


for index, row in data.iterrows():
    # resetting knowledge base each time
    env.reset()

    # split into endo and concomitant disease dicts
    endo_data = data.loc[index, ['abdominal_pelvic_pain', 'dysmenorrhea', 'pain_with_sex', 'dyschezia', 'dysuria', 'infertility', 'pelvic_perineal_pain']]
    additional_disease_data = data.loc[index, ['amenorrhea', 'constipation', 'diarrhea', 'flank_pain', 'hematuria', 'frequent_urination', 'adenomyosis']]


    # create dictionary from current row, populated only with the symptoms I need
    endo_dict = endo_data.to_dict()
    other_diseases_dict = additional_disease_data.to_dict()

    # convert all the data into types as clips Symbol: 0 -> no, 1 -> yes, '' -> unknown
    for key, value in endo_dict.items():
        curr_value = value
        if curr_value == 0:
            endo_dict[key] = clips.Symbol('no')
        elif curr_value == 1:
            endo_dict[key] = clips.Symbol('yes')
        elif curr_value == '':
            endo_dict[key] = clips.Symbol('unknown')
            # this doesn't seem to ever get used but leaving it in for robustness

    for key, value in other_diseases_dict.items():
        curr_value = value
        if curr_value == 0:
            other_diseases_dict[key] = clips.Symbol('no')
        elif curr_value == 1:
            other_diseases_dict[key] = clips.Symbol('yes')
        elif curr_value == '':
            other_diseases_dict[key] = clips.Symbol('unknown')
            # this doesn't seem to ever get used but leaving it in for robustness

    # print(concom_dict)

    # populate those into the templates using assert_fact
    patient_endo_template.assert_fact(**endo_dict)
    patient_concomitant_disease_template.assert_fact(**other_diseases_dict)

    env.run()

    print("___________CURRENT FACTS___________")
    print_facts(env)
    # EVALUATION PART

    results_data = data.loc[index, ['endometriosis', 'adenomyosis', 'ibs', 'interstitial_cystitis']]
    if results_data['endometriosis'] == 1 and results_data['adenomyosis'] == 0 and results_data['ibs'] == 0 and results_data['interstitial_cystitis'] == 0:
        evaluation_dict['only_endo_actual'] += 1
    elif results_data['endometriosis'] == 1 and (results_data['adenomyosis'] == 1 or results_data['ibs'] == 1 or results_data['interstitial_cystitis'] == 1):
        evaluation_dict['both_endo_concomitant_actual'] += 1
    elif results_data['endometriosis'] == 0 and results_data['adenomyosis'] == 0 and results_data['ibs'] == 0 and results_data['interstitial_cystitis'] == 0:
        evaluation_dict['neither_endo_concomitant_actual'] += 1
    elif results_data['endometriosis'] == 0 and (results_data['adenomyosis'] == 1 or results_data['ibs'] == 1 or results_data['interstitial_cystitis'] == 1):
        evaluation_dict['only_concomitant_actual'] += 1

print(f"{evaluation_dict['only_endo_predicted']}, {evaluation_dict['only_endo_actual']}")
print(f"{evaluation_dict['only_concomitant_predicted']}, {evaluation_dict['only_concomitant_actual']}")
print(f"{evaluation_dict['both_endo_concomitant_predicted']}, {evaluation_dict['both_endo_concomitant_actual']}")
print(f"{evaluation_dict['neither_endo_concomitant_predicted']}, {evaluation_dict['neither_endo_concomitant_actual']}")
