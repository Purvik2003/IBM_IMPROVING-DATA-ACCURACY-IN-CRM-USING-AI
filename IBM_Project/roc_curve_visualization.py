import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# Load anomaly data
df = pd.read_csv("anomaly_detected.csv")

# Convert anomaly_score (-1 = Anomaly, 1 = Normal) to binary classification
y_true = np.where(df["anomaly_score"] == -1, 1, 0)  # 1 = Fraud, 0 = Normal
y_scores = np.random.rand(len(y_true))  # Simulated anomaly scores (replace with model scores if available)

# Compute ROC Curve
fpr, tpr, _ = roc_curve(y_true, y_scores)
roc_auc = auc(fpr, tpr)

# Plot ROC Curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color="blue", lw=2, label="ROC curve (area = {:.2f})".format(roc_auc))
plt.plot([0, 1], [0, 1], color="gray", linestyle="--")  # Diagonal line
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve for Anomaly Detection")
plt.legend(loc="lower right")
plt.show()
