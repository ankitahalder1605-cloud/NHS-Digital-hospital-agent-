import pandas as pd

print("📊 NHS Digital Hospital Agent")
print("📈 Data Analysis Module")
print("=" * 40)

# Load cleaned dataset
df = pd.read_csv("../data/processed/cleaned_hospital_data.csv")

print("\n📐 Dataset Shape:")
print(df.shape)

print("\n📋 Column Names:")

for column in df.columns:
    print("•", column)

print("\n🔢 Data Types:")
print(df.dtypes)

print("\n📊 Statistical Summary:")
print(df.describe(include="all"))

print("\n✅ Data analysis completed!")
