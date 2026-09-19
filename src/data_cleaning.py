import pandas as pd

print("🏥 NHS Digital Hospital Agent")
print("📊 Data Cleaning Module")
print("=" * 40)

# Load dataset
df = pd.read_csv("../data/raw/hospital_data.csv")

print("\n📐 Dataset Shape:")
print(df.shape)

print("\n📋 First Five Records:")
print(df.head())

print("\n🔎 Missing Values:")
print(df.isnull().sum())

print("\n🔁 Duplicate Records:")
print(df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

print("\n✅ Duplicate records removed.")

# Save cleaned dataset
df.to_csv(
    "../data/processed/cleaned_hospital_data.csv",
    index=False
)

print("\n🎉 Data cleaning completed successfully!")
