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

### Sample Output

```text
Day 1:
Irrigation probability: 94.92%
Recommendation: Irrigation Needed

Day 2:
Irrigation probability: 86.10%
Recommendation: Irrigation Needed

Day 3:
Irrigation probability: 74.95%
Recommendation: Irrigation Needed
```

### Result Analysis

The model estimates the probability of irrigation being needed using soil moisture, temperature, and rainfall information. The probability decreases over the three days, but irrigation is still recommended on each day.

### Conclusion

The project demonstrates a simplified Dynamic Bayesian Network (DBN)-style probabilistic model that updates irrigation predictions over time using state transitions and observed environmental conditions.
