import pandas as pd
import os

# Define paths
input_path = "data/input/NG00102_dataset.csv"
output_path = "data/output/prepared_proteins.csv"

def prepare_data(input_file, output_file):
    df = pd.read_csv(input_file)
    # Tissue-specific segregation
    df_brain = df[df['Tissue'] == 'Brain']
    df_csf = df[df['Tissue'] == 'CSF']
    df_plasma = df[df['Tissue'] == 'Plasma']
    
    # Combine and save filtered results
    combined = pd.concat([df_brain, df_csf, df_plasma])
    combined.to_csv(output_file, index=False)
    print(f"Prepared data saved to {output_file}")

if __name__ == "__main__":
    prepare_data(input_path, output_path)
