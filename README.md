# Street Vitality from Grid-level Texture Fluctuations

This repository provides a reproducible implementation of a texture-based method for quantifying street vitality using street view imagery.

The method computes grayscale texture fluctuations at the grid level and aggregates them into proxy vitality values across different street components (sidewalks, roadways, and stalls), enabling fine-grained spatial analysis of urban vitality.

---

## 1. System requirements

The code was tested on:

- Windows 10 / Windows 11  
- Python 3.10  
- Anaconda environment  

No non-standard hardware is required for the demo. GPU acceleration is optional for large-scale CLIP inference.

---

## 2. Installation

Create a Python environment and install dependencies:

```bash
conda create -n vendor_streetview python=3.10 -y
conda activate vendor_streetview
pip install -r requirements.txt
```
Typical installation time on a standard desktop computer is approximately 5–10 minutes.

## 3. Demo

A small demo dataset is provided to illustrate the workflow.

- Run the demo:
- python run_demo.py
  
- Input：
- demo_data/demo_clip_scores.csv
  
- This file contains a simplified example of grid-level observations with the following fields:
- street_id: street segment identifier
- lap_mean: grayscale texture intensity
- ROI: region of interest (sidewalk / roadway / stall)
- clip_score: semantic score derived from image analysis

- Output：
- outputs/demo_result.csv
  
- The output includes:
- Grid-level proxy vitality values
- ROI-level aggregated vitality
- Street-level vitality indicators
  
- Expected runtime：
- Less than 1 minute on a standard desktop computer
  
## 4. Instructions for use (full pipeline)

To apply the method to your own data:

- Step 1: Prepare input data

- Your dataset should include at least the following columns:

- street_id
- lap_mean
- ROI (sidewalk, roadway, stall)
- clip_score (optional, for extended analysis)

- Step 2: Run the analysis
- python run_demo.py
- (For extended workflows, modular scripts can be placed under /src.)

- Step 3: Outputs
- The pipeline generates:
- Grid-level vitality estimates
- ROI-level vitality aggregation
- Street-level vitality indices

## 5. Reproducibility

All quantitative results presented in the manuscript can be reproduced using:

- run_demo.py (demonstration workflow)
- The provided demo dataset
- The analytical pipeline follows a deterministic procedure without stochastic components.
  
## 6. Code availability

The code supporting this study is available at:
- https://github.com/jackdhdjdbdjdbdjidodod79-byte/global-informal-economy-streetview

## 7. Data availability

A sample dataset is included in the repository for demonstration purposes.
- Due to data volume and licensing constraints, the full dataset used in the study is available from the corresponding author upon reasonable request.

## 8. License

This project is licensed under the MIT License. See the LICENSE file for details.  
