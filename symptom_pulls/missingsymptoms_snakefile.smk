configfile: 'new_config_pheno.yaml'

# snakemake -c1 Pheno/PMBB_2.3_pheno_covars.csv -s missingsymptoms_snakefile.smk
# snakemake --snakefile missingsymptoms_snakefile.smk -c1 --use-envmodules all

include: '/project/ssverma_shared/tools/lindsay_snakemake_workflows/basic_phenotyping/Snakefile'

rule all:
    input: 'Pheno/PMBB_2.3_pheno_covars.csv'