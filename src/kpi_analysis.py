import pandas as pd

print("📊 NHS Digital Hospital Agent")
print("📈 KPI Analysis Module")
print("=" * 40)

# Load cleaned dataset
df = pd.read_csv("../data/processed/cleaned_hospital_data.csv")

print(f"\n👥 Total Records: {len(df):,}")
print(f"📋 Total Variables: {len(df.columns)}")

print("\n📊 Available Variables:")

for column in df.columns:
    print("•", column)

print("\n🔢 Numeric Variables:")

numeric_columns = df.select_dtypes(
    include="number"
).columns

for column in numeric_columns:
    print(
        f"• {column}: "
        f"Average = {df[column].mean():.2f}"
    )

print("\n🎉 KPI exploration completed!")
