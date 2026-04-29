# Global Informal Economy from Street View Imagery

This repository contains the code and a demonstration dataset for the study:

**"Environmental constraints shape informal economic behaviour across global cities"**

submitted to *Nature Human Behaviour*.

---

## 1. Overview

This project quantifies informal economic activity (street vendors) at a global scale using street view imagery and vision–language models (CLIP).

Instead of relying on manual surveys or headcounts, we extract a **vendor activity index** directly from images, enabling consistent, scalable measurement across diverse urban contexts.

---

## 2. Data Description

### Demo dataset

A small demonstration dataset is provided:

demo_data/demo_clip_scores.csv
  
This file includes:

- `city_id` — unique city identifier  
- `country_iso2` — ISO country code  
- `city_name` — city name  
- `city_role` — Metropolitan / Livability  
- `street_id` — street segment identifier  
- `image_id` — street view image ID  
- `lat`, `lon` — geographic coordinates  
- `captured_at` — timestamp (UTC)  
- `vendor_score` — CLIP-derived vendor activity score  

Note:  
This dataset is a **small subset for demonstration only**.  
The full dataset used in the study contains ~250,000+ images and is not publicly released due to platform restrictions.

---

## 3. System Requirements

The code was tested on:

- Windows 10 / Windows 11  
- Python 3.10  
- Anaconda environment  

No non-standard hardware is required. GPU is optional (for large-scale CLIP inference only).

---

## 4. Installation

Create a Python environment and install dependencies:

```bash
conda create -n vendor_streetview python=3.10 -y
conda activate vendor_streetview
pip install -r requirements.txt
```
Typical installation time: 5–10 minutes on a standard desktop computer.

## 5. Demo: Running the code

Run the demo script:

python run_demo.py

This will:

- Load the demo dataset
- Aggregate vendor scores at street level
- Compute simple statistics
- Output summary results

## 6. Expected Output

The script prints:

- Mean vendor score
- Distribution summary
- Aggregated street-level statistics

Example output:

- Mean vendor score: 0.41
- Number of images: 20
- Number of streets: 10

Expected runtime: < 5 seconds

## 7. Reproducibility

To reproduce the main analytical workflow:

- Collect street view images via Mapillary API
- Apply CLIP model to extract vendor-related semantic scores
- Aggregate scores at image → street → city levels
- Conduct statistical analysis (correlation, regression, distribution analysis)

Due to API and data licensing constraints, only a demonstration dataset is provided here.

## 8. Software and Dependencies

Key Python packages:

- pandas
- numpy
- matplotlib
- scikit-learn

Full list available in:

requirements.txt

## 9. Code Availability

All code used in this study is available in this repository.

The repository includes:

- Data processing scripts
- Demonstration dataset
- Reproducible analysis pipeline

## 10. Data Availability

The demo dataset is included in this repository.

The full dataset is not publicly shared due to:

Platform usage restrictions (Mapillary)
Data size constraints

However, all analytical procedures are fully reproducible. 

## 11. License

This project is released under the MIT License.

## 12. Contact

For questions, please contact:

Yan Gui:971463944@qq.com

## 13. Notes for Reviewers

This repository is designed to allow reviewers to:

- Run the code without additional setup
- Verify analytical logic
- Inspect data structure and outputs

No external data download is required for the demo.

The scripts in the `src/` folder provide the full analytical workflow. 

However, for demonstration and reproducibility, users only need to run `run_demo.py`.


