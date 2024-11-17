import pandas as pd

# Paths
input_file = "data/output/structural_analysis.csv"
output_file = "data/output/disease_pathways.csv"

def map_pathways(input_file, output_file):
    df = pd.read_csv(input_file)
    df['Disease Relevance'] = df['PDB File'].apply(lambda x: "Alzheimer's" if "brain" in x else "Parkinson's")
    df.to_csv(output_file, index=False)
    print(f"Disease pathway mapping saved to {output_file}")

if __name__ == "__main__":
    map_pathways(input_file, output_file)
