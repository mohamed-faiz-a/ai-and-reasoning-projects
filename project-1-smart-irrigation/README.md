# Smart Irrigation Prediction

## Problem Statement
Predict whether irrigation is required based on soil moisture, temperature, and rainfall.

## Inputs
- Soil moisture: Low, Medium, High
- Temperature: High, Normal
- Rainfall: Yes or No

## AI Technique
Dynamic Bayesian Network (DBN)-style probabilistic model.

## Expected Output
Irrigation probability and a watering recommendation for each day.

## Sample Results

| Day | Irrigation Probability | Recommendation |
|---|---:|---|
| 1 | 91.30% | Irrigation Needed |
| 2 | 85.08% | Irrigation Needed |
| 3 | 62.49% | Irrigation Needed |

## Conclusion
The model estimates irrigation needs using soil moisture, temperature, and rainfall observations. In this sample, the probability of irrigation being needed decreases from Day 1 to Day 3.

## Implementation
- Python
- NumPy

## Note
This is a simplified educational model with illustrative probabilities, not a validated real-world irrigation system.
