import os

# Paths
input_fasta = "data/input/proteins.fasta"
output_dir = "data/output/alphafold_predictions/"

def run_alphafold(fasta_path, output_path):
    # Ensure output directory exists
    os.makedirs(output_path, exist_ok=True)

    # AlphaFold 3 command
    os.system(f"""
        python alphafold/run_alphafold.py \
        --fasta_path={fasta_path} \
        --output_dir={output_path} \
        --model_preset=monomer
    """)
    print(f"AlphaFold predictions saved to {output_path}")

if __name__ == "__main__":
    run_alphafold(input_fasta, output_dir)
