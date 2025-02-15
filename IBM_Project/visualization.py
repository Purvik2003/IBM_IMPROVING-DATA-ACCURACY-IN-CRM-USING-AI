import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load anomaly data
df = pd.read_csv("anomaly_detected.csv")

# Plot anomaly distribution
plt.figure(figsize=(8,5))
sns.countplot(x=df["anomaly_score"])
plt.title("Anomaly Detection Results")
plt.xlabel("Anomaly Score (-1 = Anomaly, 1 = Normal)")
plt.ylabel("Count")
plt.show()
