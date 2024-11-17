import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Paths
input_file = "data/output/structural_analysis.csv"
output_dir = "data/output/visualizations/"

def create_visualizations(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(input_file)
    
    # Example: Sequence Length Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Sequence Length'], kde=True, color='blue')
    plt.title("Sequence Length Distribution")
    plt.savefig(os.path.join(output_dir, "sequence_length_distribution.png"))
    plt.close()

    print(f"Visualizations saved to {output_dir}")

if __name__ == "__main__":
    create_visualizations(input_file, output_dir)
