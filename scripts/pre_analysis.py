from pandasgwas.get_variants import get_variants_by_reported_trait
import pandas as pd

'''
*** STEP 2: DETERMINE INFLUENTIAL COMORBID GENES ***
The goal of the methods below is to create a limited list of genes that can be controlled for in the final GWAS.
These genes should be influential in both their relevant comorbidity and the primary disease.
'''

# Main function to 
# n: Upper threshold for number of genetic variants
def get_comorbid_variants(cmb_csv, api, n = 100):
    # Read in comorbidities for each variant
    cmb_csv.drop(list(cmb_csv.filter(regex = 'Prevalence')), axis=1, inplace=True)
    primary_diseases = cmb_csv.columns # List of each disease of interest
    # TODO: remove code block below. Kept during initial development phase.
    banned = ['males', 'females']
    remove_words = lambda x: ' '.join([item for item in x.split() if item not in banned])
    cmb_csv = {col: cmb_csv[col].apply(remove_words) for col in cmb_csv.columns}
    #
    # Create dictionary to store variants (SNPs only for now)
    variants = {key for key in pd.unique(cmb_csv).values.ravel('K')}
    variants = variants | {key: [] for key in primary_diseases}

    # Get variants as gene names
    for v in variants.keys:
        variants[v] = call_gwas_api(api) 

    tmp = variants[0] #TODO: through which VariantObject attribute(s) can we get the genetic variants?
    variants_df = pd.DataFrame(variants)
    variants_df.map(lambda x: x)

    # Intersect with respective primary disease
    significant_variants = pd.DataFrame.from_dict(columns=cmb_csv.columns)

    for pd in significant_variants.columns:
        significant_variants = variants[pd]
    
    # For each comorbidity (within each primary_disease)
        # search the GWAS catalog for keywords.
        # Get: gene name, association strength, association direction
        # Result: List of ALL significant genetic variants for a primary_disease -> cmb_variants
        # Intersect cmb_variants, pd_variants


    #TODO: how will you deal with comorbidities only influential in males? or certain ethnicities?
    #


# Wrapper function to call different APIs
def call_gwas_api(option):
    if option == 'opengwas':
        return get_variants_by_reported_trait(v)
    elif option == 'nih':
        return []