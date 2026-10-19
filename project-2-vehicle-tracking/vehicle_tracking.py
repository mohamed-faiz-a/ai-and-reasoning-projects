import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)

n = 30
actual = np.arange(n) * 2.0
measured = actual + np.random.normal(0, 5, n)

state = np.array([measured[0], 2.0])
P = np.eye(2) * 10

F = np.array([[1, 1], [0, 1]])
H = np.array([[1, 0]])
Q = np.eye(2) * 0.1
R = np.array([[25.0]])

estimated = []

for z in measured:
    state = F @ state
    P = F @ P @ F.T + Q

    K = P @ H.T @ np.linalg.inv(H @ P @ H.T + R)
    state = state + (K @ (np.array([z]) - H @ state)).flatten()
    P = (np.eye(2) - K @ H) @ P

    estimated.append(state[0])

estimated = np.array(estimated)

print("Measurement RMSE:", round(np.sqrt(np.mean((measured - actual)**2)), 2))
print("Estimated RMSE:", round(np.sqrt(np.mean((estimated - actual)**2)), 2))

plt.plot(actual, label="Actual Position")
plt.scatter(range(n), measured, label="GPS Measurements")
plt.plot(estimated, label="Kalman Estimate")
plt.xlabel("Time")
plt.ylabel("Position")
plt.title("Vehicle Position Estimation")
plt.legend()
plt.show()
