import pandas as pd
from fuzzywuzzy import process

# Load cleaned CRM data
df = pd.read_csv("cleaned_crm_data.csv")

# Function for correcting names
def correct_names(name, choices):
    best_match = process.extractOne(name, choices)
    return best_match[0] if best_match and best_match[1] > 80 else name

# Apply name corrections
df["First Name"] = df["First Name"].apply(lambda x: correct_names(x, df["First Name"].unique()))
df["Last Name"] = df["Last Name"].apply(lambda x: correct_names(x, df["Last Name"].unique()))

# Save corrected dataset
df.to_csv("final_cleaned_data.csv", index=False)

print("✅ Name correction completed successfully!")
