# Vehicle Position Estimation

## Problem Statement
Estimate a vehicle's position from noisy GPS measurements using Kalman Filtering.

## Inputs
- Simulated actual vehicle positions
- Noisy GPS measurements
- Process noise and measurement noise values

## AI Technique
Kalman Filtering.

## Expected Output
Estimated vehicle positions, a comparison graph, and RMSE values.

## Results

| Metric | RMSE |
|---|---:|
| GPS Measurement | 5.28 |
| Kalman Estimate | 3.18 |

## Analysis
The Kalman filter reduced the RMSE from 5.28 to 3.18, an approximate 39.8% reduction in estimation error for this simulation.

The graph compares the actual positions, noisy GPS measurements, and Kalman-filter estimates.

## Conclusion
The results demonstrate how Kalman Filtering can improve vehicle position estimates by combining motion predictions with noisy GPS measurements.

## Implementation
- Python
- NumPy
- Matplotlib
