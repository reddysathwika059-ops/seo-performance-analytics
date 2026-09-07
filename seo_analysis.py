import pandas as pd
import matplotlib.pyplot as plt

# Sample SEO data
data = {
    "Keyword": [
        "python course",
        "data analytics",
        "machine learning",
        "sql tutorial",
        "excel course",
        "power bi tutorial"
    ],
    "Clicks": [120, 95, 80, 65, 50, 45],
    "Impressions": [5000, 4200, 3800, 3000, 2800, 2500],
    "Position": [4.2, 6.1, 7.5, 9.2, 11.4, 13.1]
}

df = pd.DataFrame(data)

# Calculate CTR
df["CTR"] = (df["Clicks"] / df["Impressions"]) * 100

print(df)
print("\nBest Keyword:")
print(df.loc[df["CTR"].idxmax()])

print("\nWorst Keyword:")
print(df.loc[df["CTR"].idxmin()])
print("\nAverage CTR:", df["CTR"].mean())
print("Average Position:", df["Position"].mean())
plt.bar(df["Keyword"], df["CTR"])
plt.xlabel("Keyword")
plt.ylabel("CTR (%)")
plt.title("CTR by Keyword")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
df.to_excel("seo_report.xlsx", index=False)