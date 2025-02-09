from pre_analysis import *


def main():
    # Inputs
    n = 200 # Upper limit of variants 
    primary_diseases = [[]] # Nested list; a list of keywords/IDs for each disease of interest

    # Call the pipeline
    comorbid_variants = get_comorbid_variants(primary_diseases, n)




main()