import pandas as pd
import matplotlib.pyplot as plt

# Load the anomaly detection results
df = pd.read_csv("anomaly_detected.csv")

# Count anomalies and normal transactions
anomaly_counts = df["anomaly_score"].value_counts()
labels = ["Normal Transactions", "Anomalies"]

# Plot Pie Chart
plt.figure(figsize=(6,6))
plt.pie(anomaly_counts, labels=labels, autopct="%1.1f%%", colors=["lightblue", "red"], startangle=90)
plt.title("Anomaly Distribution in CRM Data")
plt.show()
