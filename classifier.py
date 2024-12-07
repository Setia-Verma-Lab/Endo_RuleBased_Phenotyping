# import clips
# import sys
# sys.path.append('./src/')
# from clips_util import print_facts, print_rules, print_templates, build_read_assert

# # create the CLIPS environment
# env = clips.Environment()

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



import clips

DEFTEMPLATE_STRING = """
(deftemplate person
  (slot name (type STRING))
  (slot surname (type STRING))
  (slot birthdate (type SYMBOL)))
"""

DEFRULE_STRING = """
(defrule hello-world
  "Greet a new person."
  (person (name ?name) (surname ?surname))
  =>
  (println "Hello " ?name " " ?surname))
"""

environment = clips.Environment()

# define constructs
environment.build(DEFTEMPLATE_STRING)
environment.build(DEFRULE_STRING)

# retrieve the fact template
template = environment.find_template('person')

# assert a new fact through its template
fact = template.assert_fact(name='John',
                            surname='Doe',
                            birthdate=clips.Symbol('01/01/1970'))

# fact slots can be accessed as dictionary elements
assert fact['name'] == 'John'

# execute the activations in the agenda
environment.run()

# read in input from csv file

