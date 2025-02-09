from pandasgwas import get_studies


'''
*** STEP 2: DETERMINE INFLUENTIAL COMORBID GENES ***
The goal of the methods below is to create a limited list of genes that can be controlled for in the final GWAS.
These genes should be influential in both their relevant comorbidity and the primary disease.
'''

# Main function to 
# n: Upper threshold for number of genetic variants
# primary_diseases: Nested list; a list of keywords/IDs for each disease of interest
def get_comorbid_variants(primary_diseases = [[]], n = 100):
    # For each primary_disease
        # Get comorbidities
        # Get: gene name, association strength, association direction -> pd_variants
    
    # For each comorbidity (within each primary_disease)
        # search the GWAS catalog for keywords.
        # Get: gene name, association strength, association direction
        # Result: List of ALL significant genetic variants for a primary_disease -> cmb_variants
        # Intersect cmb_variants, pd_variants

