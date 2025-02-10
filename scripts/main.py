from pre_analysis import *


def main():
    # Inputs
    n = 200 # Upper limit of variants 
    primary_diseases = [[]] # Nested list; a list of keywords/IDs for each disease of interest
    gwas_api = 'opengwas' # Options: 'opengwas', 'nih'

    # Call the pipeline
    # Output: list of significant GVs for every disease of interest 
    #NOTE: the GWAS API is currently limited to SNPs
    cmb_csv = pd.read_csv('input/comorbidities copy.csv')
    comorbid_variants = get_comorbid_variants(cmb_csv, gwas_api, n)


main()