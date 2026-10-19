import numpy as np

states = ["Irrigation Needed", "Not Needed"]

belief = np.array([0.4, 0.6])

no_rain = np.array([
    [0.8, 0.2],
    [0.4, 0.6]
])

rain_transition = np.array([
    [0.3, 0.7],
    [0.1, 0.9]
])

moisture_prob = {
    "Low": [0.9, 0.1],
    "Medium": [0.5, 0.5],
    "High": [0.1, 0.9]
}

temperature_prob = {
    "High": [0.7, 0.4],
    "Normal": [0.3, 0.6]
}

moisture = ["Low", "Medium", "Low"]
temperature = ["High", "High", "Normal"]
rainfall = ["No", "No", "Yes"]

for t in range(len(moisture)):
    if t > 0:
        matrix = (
            rain_transition
            if rainfall[t] == "Yes"
            else no_rain
        )
        belief = belief @ matrix

    likelihood = (
        np.array(moisture_prob[moisture[t]])
        * np.array(temperature_prob[temperature[t]])
    )

    belief = belief * likelihood
    belief = belief / belief.sum()

    print(f"Day {t + 1}:")
    print(f"Irrigation probability: {belief[0]:.2%}")
    print(f"Recommendation: {states[np.argmax(belief)]}")
    print()
