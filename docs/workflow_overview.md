# Workflow overview

The analysis converts street-view imagery into street- and city-level vendor activity indicators.

## Step 1. Image metadata processing

Street-view image metadata include image ID, coordinates, timestamp, city ID and street ID.

## Step 2. Vendor semantic scoring

Each image is evaluated using CLIP-based semantic prompts related to vendor activity. The output is an image-level vendor score.

## Step 3. Street-level aggregation

Image-level scores are aggregated by street segment using mean score, detection rate and top-score statistics.

## Step 4. City-level aggregation

Street-level indices are aggregated to city-level vendor activity indicators.

## Step 5. Statistical analysis

The resulting indicators are used to examine global spatial patterns and environmental constraints on informal economic activity.
