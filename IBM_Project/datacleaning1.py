import pandas as pd
from fuzzywuzzy import process

# Load Data
df = pd.read_csv("CRM Sales.csv")

# Handling Duplicates
df.drop_duplicates(inplace=True)

# Normalize Emails (lowercase, remove spaces)
df["E-Mail"] = df["E-Mail"].str.strip().str.lower()

# Format Phone Numbers (removing spaces, dashes)
df["Phone No"] = df["Phone No"].str.replace(r"\D", "", regex=True)

# Save cleaned data
df.to_csv("cleaned_crm_data.csv", index=False)

print("✅ Data cleaning completed successfully!")
