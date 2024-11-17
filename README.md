# AlphaFold 3-Based Structural Analysis of pQTL-Derived Proteins

This repository implements a pipeline to model and analyze cis- and trans-pQTL-derived proteins implicated in neurological diseases using AlphaFold 3. The workflow integrates the NG00102 dataset for tissue-specific protein data and provides structural predictions, prioritization, and visualization.

## Workflow
1. **Data Preparation**: Extract tissue-specific protein data from the NG00102 dataset.
2. **AlphaFold Predictions**: Generate protein structure models using AlphaFold 3.
3. **Structural Analysis**: Prioritize proteins based on structural confidence and sequence length.
4. **Visualization**: Create histograms, scatter plots, and 3D annotations of proteins.
5. **Integration with Disease Pathways**: Map prioritized proteins to disease-relevant pathways.

## Getting Started
1. Install dependencies: `pip install -r requirements.txt`.
2. Place input data in `data/input/`.
3. Run the pipeline:
   ```bash
   python scripts/data_preparation.py
   python scripts/run_alphafold.py
   python scripts/analyze_structures.py
   python scripts/visualize_results.py
   python scripts/map_disease_pathways.py
