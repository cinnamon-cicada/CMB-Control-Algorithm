# Comorbidity Control Algorithm

## About
The overarching goal of this project is to test a novel method for controlling for comorbidities. 

## Setup
1. 

## Workflow (Pseudocode)
0. Inputs
    1. Case/control populations
        1. Control for noise using patient matching
    2. Phecodes: PheWAS-generated most common comorbidities, represented as phecodes
1. Find genetic variants (GVs) linked to each phecode from previous GWAS
    1. PLINK: Find all linked genes for each comorbidity phenotype (CP)
    2. GWAS (PandasGWAS): Library of established GWAS associations
2. Run GWAS
    1. Covariates: sex, age range, ethnicity
    2. Library: PLINK
    3. Algorithms
        1. Method 1: Use all GVs as binary variates
            1. 1x with each Comorbidity GVs as a covariate
            2. 1x without
        2. Method 2: 
3. Analysis
    1. Noise between 1. including and 2. exclusing comorbidity SNPs
4. 

## File Structure
├── README.md
├── scripts/
│   ├── algorithm.py      # Comorbidity control algorithm(s)
│   ├── pre_analysis.py   # Establish need
│   ├── post_analysis.py   # Evaluate algorithm
│   ├── main.py   # Run algorithm
├── output/
│   ├──    # [as needed]

## Technology
- Python: Numpy, Pandas
- R: PheWAS, GWAS
- Google BigQuery (SQL)

## Future Work