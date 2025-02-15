import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned CRM data
df = pd.read_csv("cleaned_crm_data.csv")

# Compute correlation matrix
corr_matrix = df.corr()

# Plot heatmap
plt.figure(figsize=(10,6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned CRM data
df = pd.read_csv("cleaned_crm_data.csv")

# Compute correlation matrix
corr_matrix = df.corr()

# Plot heatmap
plt.figure(figsize=(10,6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()
