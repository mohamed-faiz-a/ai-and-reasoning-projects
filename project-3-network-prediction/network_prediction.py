import numpy as np

states = ["Normal", "Busy", "Congested"]
observations = ["Low", "Medium", "High"]

start = np.array([0.6, 0.3, 0.1])

transition = np.array([
    [0.7, 0.25, 0.05],
    [0.2, 0.6, 0.2],
    [0.1, 0.3, 0.6]
])

emission = np.array([
    [0.8, 0.15, 0.05],
    [0.15, 0.7, 0.15],
    [0.05, 0.2, 0.75]
])

data = ["Low", "Medium", "High", "High", "Medium"]

score = np.zeros((len(states), len(data)))
path = np.zeros((len(states), len(data)), dtype=int)

score[:, 0] = start * emission[:, observations.index(data[0])]

for t in range(1, len(data)):
    for s in range(len(states)):
        values = score[:, t - 1] * transition[:, s]
        path[s, t] = np.argmax(values)
        score[s, t] = (
            np.max(values)
            * emission[s, observations.index(data[t])]
        )

last = np.argmax(score[:, -1])
result = [last]

for t in range(len(data) - 1, 0, -1):
    last = path[last, t]
    result.append(last)

result.reverse()

print("Observed Traffic:", data)
print("Predicted Network States:")

for traffic, state_index in zip(data, result):
    print(f"{traffic} -> {states[state_index]}")
