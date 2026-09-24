from sklearn.ensemble import IsolationForest
import numpy as np

# Normal network traffic
normal_traffic = np.array([
    [15], [16], [17], [18], [19],
    [20], [21], [22], [23], [24],
    [25], [18], [20], [22], [24],
    [19], [21], [23], [17], [25]
])

model = IsolationForest(
    n_estimators=200,
    contamination=0.1,
    random_state=42
)

model.fit(normal_traffic)

print("🛡️ CyberNexus Anomaly Detection")
print("--------------------------------")

traffic = float(input("Enter packets per second: "))

prediction = model.predict([[traffic]])

# Extra boundary check for this educational demo
if prediction[0] == -1 or traffic < 10 or traffic > 30:
    print("⚠️ Anomaly detected!")
else:
    print("✅ Normal network traffic.")