# Comorbidity Control Algorithm

## About
The overarching goal of this project is to test a novel method for controlling for comorbidities. 

## Setup
1. 

## Workflow (Pseudocode)
0. Inputs
    1. Case/control populations
        1. 
    2. Phecodes: PheWAS-generated most common comorbidities, represented as phecodes
1. Find genetic variants linked to each phecode from previous GWAS
    1. PLINK: Find all linked genes for each comorbidity phenotype (CP)
    2. GWAS (PandasGWAS): Library of established GWAS associations
2. Run GWAS
    1. Covariates: comorbidity SNPs (binary), sex, age range, ethnicity
    2. Library: PLINK
3. 
4. 

## File Structure
├── README.md
├── scripts/
│   ├── algorithm.py
│   ├── ats_search.py

## Technology
- Python: Numpy, Pandas
- R: PheWAS, GWAS
- Google BigQuery (SQL)

## Future Work