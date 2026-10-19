# Network Activity Prediction

## Problem Statement
Infer hidden network conditions from observed traffic levels using a Hidden Markov Model.

## Inputs
- Traffic observations: Low, Medium, High
- Initial state probabilities
- State transition probabilities
- Observation probabilities

## AI Technique
Hidden Markov Model (HMM) using the Viterbi algorithm.

## Expected Output
The most likely sequence of hidden network states based on observed traffic.

## Sample Results

| Observed Traffic | Predicted Network State |
|---|---|
| Low | Normal |
| Medium | Busy |
| High | Congested |
| High | Congested |
| Medium | Busy |

## Analysis
The model identifies Normal, Busy, and Congested network conditions from the five sample traffic observations.

## Conclusion
The HMM and Viterbi algorithm estimate the most likely sequence of hidden network states from observed traffic levels.

## Implementation
- Python
- NumPy

## Note
This is an educational simulation using illustrative probabilities, not a validated real-world network monitoring system.
