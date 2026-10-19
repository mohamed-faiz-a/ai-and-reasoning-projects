# Network Activity Prediction

## Problem Statement
Infer network conditions from observed traffic levels.

## Inputs
- Low, medium, or high traffic observations
- Initial probabilities
- Transition probabilities
- Observation probabilities

## AI Technique
Hidden Markov Model (HMM), using the Viterbi algorithm.

## Expected Output
The most likely sequence of network states.

## Evaluation
Compare predicted states with known sample states.

## Implementation
Python and NumPy.
