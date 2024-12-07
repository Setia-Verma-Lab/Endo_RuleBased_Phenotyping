import clips
import pandas as pd
import sys
sys.path.append('./src/')
from clips_util import print_facts, print_rules, print_templates, build_read_assert

# create the CLIPS environment
env = clips.Environment()

# # basic patient information
# DEFTEMPLATE_PATIENT = """
# (deftemplate patient 
#     (slot name_is (type STRING))
#     (slot age_is (type INTEGER))
#     )
# """
# env.build(DEFTEMPLATE_PATIENT)

# # participant pelvic pain
# DEFTEMPLATE_ACUTE_PELVIC_PAIN = """
# (deftemplate pelvic_pain
#     (slot has_pain (type SYMBOL)
#         (allowed-symbols yes no unknown))
# )
# """
# env.build(DEFTEMPLATE_ACUTE_PELVIC_PAIN)

# # participant Karnofsky quality of life score
# DEFTEMPLATE_DYSMENORRHEA = """
# (deftemplate dysmenorrhea
#   (slot has_dysmenorrhea (type SYMBOL)
#     (allowed-symbols yes no unknown))
# )
# """
# env.build(DEFTEMPLATE_DYSMENORRHEA)

# # participant HIV ELISA test result
# DEFTEMPLATE_DYSPAREUNIA = """
# (deftemplate dyspareunia
#     (slot has_dyspareunia (type SYMBOL)
#         (allowed-symbols yes no unknown))
# )
# """
# env.build(DEFTEMPLATE_DYSPAREUNIA)

# # participant dyschezia status
# DEFTEMPLATE_DYSCHEZIA = """
# (deftemplate dyschezia
#    (slot has_dyschezia (type SYMBOL)
#         (allowed-symbols yes no unknown)))
# """
# env.build(DEFTEMPLATE_DYSCHEZIA)

# # participant dysuria status
# DEFTEMPLATE_DYSURIA = """
# (deftemplate dysuria
#    (slot has_dysuria (type SYMBOL)
#         (allowed-symbols yes no unknown)))
# """
# env.build(DEFTEMPLATE_DYSURIA)

# # participant pregnancy status
# DEFTEMPLATE_INFERTILITY = """
# (deftemplate infertility    
#     (slot is_infertile (type SYMBOL)
#         (allowed-symbols yes no unknown))
# )
# """
# env.build(DEFTEMPLATE_INFERTILITY)

# # participant chronic pelvic pain
# DEFTEMPLATE_CHRONIC_PELVIC_PAIN = """
# (deftemplate chronic_pelvic_pain
#     (slot has_chronic_pelvic_pain (type SYMBOL)
#         (allowed-symbols yes no unknown))
# )
# """
# env.build(DEFTEMPLATE_CHRONIC_PELVIC_PAIN)

# # participant has amenorrhea
# DEFTEMPLATE_AMENORRHEA = """
# (deftemplate amenorrhea
#     (slot has_amenorrhea (type SYMBOL) 
#         (allowed-symbols yes no unknown))
# )
# """
# env.build(DEFTEMPLATE_AMENORRHEA)

# # participant constipation status
# DEFTEMPLATE_CONSTIPATION = """
# (deftemplate constipation
#     (slot has_constipation (type SYMBOL)
#         (allowed-symbols yes no unknown))
# )
# """
# env.build(DEFTEMPLATE_CONSTIPATION)

# # participant diarrhea status
# DEFTEMPLATE_DIARRHEA = """
# (deftemplate diarrhea
#     (slot has_diarrhea (type SYMBOL)
#         (allowed-symbols yes no unknown))
# )
# """
# env.build(DEFTEMPLATE_DIARRHEA)

# # participant flank pain status
# DEFTEMPLATE_FLANK_PAIN = """
# (deftemplate flank_pain
#     (slot has_flank_pain (type SYMBOL)
#         (allowed-symbols yes no unknown))
# )
# """
# env.build(DEFTEMPLATE_FLANK_PAIN)

# # participant hematuria status
# DEFTEMPLATE_HEMATURIA = """
# (deftemplate hematuria
#     (slot has_hematuria (type SYMBOL)
#         (allowed-symbols yes no unknown))
# )
# """
# env.build(DEFTEMPLATE_HEMATURIA)

# # participant frequent urination status
# DEFTEMPLATE_FREQUENT_URINATION = """
# (deftemplate frequent_urination
#     (slot has_frequent_urination (type SYMBOL)
#         (allowed-symbols yes no unknown))
# )
# """
# env.build(DEFTEMPLATE_FREQUENT_URINATION)

# # participant adenomyosis status
# DEFTEMPLATE_ADENOMYOSIS = """
# (deftemplate adenomyosis
#     (slot has_adenomyosis (type SYMBOL)
#         (allowed-symbols yes no unknown))
# )
# """
# env.build(DEFTEMPLATE_ADENOMYOSIS)

# # participant inclusion criteria met status
# DEFTEMPLATE_ENDOMETRIOSIS_INCLUSION = """
# (deftemplate endometriosis_inclusion
#     (slot meets_criteria (type SYMBOL)
#         (allowed-symbols yes no unknown))
# )
# """
# env.build(DEFTEMPLATE_ENDOMETRIOSIS_INCLUSION)

# # participant trial eligibility status
# DEFTEMPLATE_CONCOMITANT_DISEASE_INCLUSION = """
# (deftemplate concomitant_disease_inclusion
#     (slot meets_criteria (type SYMBOL)
#     (allowed-symbols yes no unknown possible))
# )
# """
# env.build(DEFTEMPLATE_CONCOMITANT_DISEASE_INCLUSION)

# # Add deffacts that the inclusion, exclusion, trial eligibility, and child bearing status are all unknown
# DEFFCATS_INITIAL_STATUS = """
# (deffacts starting_inclusion_exclusion_facts "Set the inclusion criteria met to unknown"
#     (endometriosis_inclusion (meets_criteria unknown))
#     (concomitant_disease_inclusion (meets_criteria unknown))
# )
# """
# env.build(DEFFCATS_INITIAL_STATUS)

# # reset the environment to make sure the deffacts are added
# env.reset()



# DEFTEMPLATE_STRING = """
# (deftemplate person
#   (slot name (type STRING))
#   (slot surname (type STRING))
#   (slot birthdate (type SYMBOL)))
# """

# DEFRULE_STRING = """
# (defrule hello-world
#   "Greet a new person."
#   (person (name ?name) (surname ?surname))
#   =>
#   (println "Hello " ?name " " ?surname))
# """

# environment = clips.Environment()

# # define constructs
# environment.build(DEFTEMPLATE_STRING)
# environment.build(DEFRULE_STRING)

# # retrieve the fact template
# template = environment.find_template('person')

# # assert a new fact through its template
# fact = template.assert_fact(name='John',
#                             surname='Doe',
#                             birthdate=clips.Symbol('01/01/1970'))

# # fact slots can be accessed as dictionary elements
# assert fact['name'] == 'John'

# # execute the activations in the agenda
# environment.run()

# read in input from csv file

# three outputs
# calculate accuracy, PPV, NPV for each case

# and ablation analysis

data_file = '/project/ssverma_shared/projects/Endometriosis/Endo_RuleBased_Phenotyping/symptom_pulls/Pheno/PMBB_2.3_pheno_covars.csv'

data = pd.read_csv(data_file, sep=',', index_col='PMBB_ID')

# print(data['chronic_pelvic_peritonitis'])

# data_dict
# patient age: CURRENT_AGE
#

# run each row at a time, then evaluate correctness and store in another object

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

# retrieve the fact templates
patient_endo_template = env.find_template('patient_endo_symptoms')
patient_concomitant_disease_template = env.find_template('patient_concomitant_disease_symptoms')

# # Find distinct values and their range
# NAME = 'infertility'
# distinct_values = data[NAME].unique()
# value_range = (distinct_values.min(), distinct_values.max())

# print(f"Distinct values in {NAME}: {sorted(distinct_values)}")
# print(f"Range of distinct values in {NAME}: {value_range}")

evaluation_dict = {'only_endo_predicted':0, 'only_endo_actual':0, 'only_concomitant_predicted':0, 'only_concomitant_actual':0, 'both_endo_concomitant_predicted':0, 'both_endo_concomitant_actual':0, 'neither_endo_concomitant_predicted':0, 'neither_endo_concomitant_actual':0}

def store_result(*args):
    endo, other = args
    if endo == "endo_0" and other == "other_0":
        evaluation_dict['neither_endo_concomitant_predicted'] += 1
    elif endo == "endo_0" and other == "other_1":
        evaluation_dict['only_concomitant_predicted'] += 1
    elif endo == "endo_1" and other == "other_0":
        evaluation_dict['only_endo_predicted'] += 1
    elif endo == "endo_1" and other == "other_1":
        evaluation_dict['both_endo_concomitant_actual'] += 1

env.define_function(store_result)

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

    print("___________CURRENT FACTS___________")
    print_facts(env)

    # env.run()
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
