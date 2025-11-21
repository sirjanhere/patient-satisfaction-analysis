import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/patient_satisfaction_2024.csv")

# Clean & prepare
df_clean = df[df["Quarter"].isin(["Q1", "Q2", "Q3", "Q4"])].copy()
df_clean["Score"] = pd.to_numeric(df_clean["Score"])

# Industry target
industry_target = 4.5

# Calculate average (should match 3.86)
calculated_avg = df_clean["Score"].mean()
print("Calculated Average:", round(calculated_avg, 2))

# Line chart for quarterly trend
plt.figure(figsize=(8,5))
plt.plot(df_clean["Quarter"], df_clean["Score"], marker="o", label="Patient Score")
plt.axhline(industry_target, linestyle="--", label="Industry Target (4.5)")
plt.title("Patient Satisfaction Score - 2024 Quarterly Trend")
plt.xlabel("Quarter")
plt.ylabel("Score")
plt.legend()
plt.tight_layout()
plt.savefig("visuals/quarterly_trend.png")

# Bar chart comparison
plt.figure(figsize=(8,5))
plt.bar(df_clean["Quarter"], df_clean["Score"])
plt.axhline(industry_target, linestyle="--")
plt.title("Quarter-wise Comparison with Industry Target")
plt.xlabel("Quarter")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig("visuals/bar_comparison.png")

print("Charts saved in visuals/ folder.")
