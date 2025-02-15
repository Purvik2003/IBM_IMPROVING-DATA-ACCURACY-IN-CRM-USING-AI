import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Load anomaly detection results
df = pd.read_csv("anomaly_detected.csv")

# Convert anomaly_score (-1 = Anomaly, 1 = Normal) to binary classification
y_true = np.where(df["anomaly_score"] == -1, 1, 0)  # 1 = Fraud, 0 = Normal
y_pred = np.where(df["anomaly_score"] == -1, 1, 0)  # Using model predictions

# Compute Confusion Matrix
cm = confusion_matrix(y_true, y_pred)

# Plot Confusion Matrix
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Normal", "Anomaly"], yticklabels=["Normal", "Anomaly"])
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix for Anomaly Detection")
plt.show()
