# Import pandas
import pandas as pd

# Import matplotlib
import matplotlib.pyplot as plt

# Load ranked catalysts
ranked = pd.read_csv(
    "results/ranked_by_prediction.csv"
)

# Select top 10 catalysts
top10 = ranked.head(10)

# Create figure
plt.figure(
    figsize=(10, 5)
)

# Create bar chart
plt.bar(
    range(len(top10)),
    top10["Predicted_Overpotential"]
)

# Add labels
plt.xlabel("Top 10 Catalysts")

plt.ylabel("Predicted Overpotential (mV)")

plt.title(
    "Top 10 Bayesian Optimization Candidates"
)

# Save figure
plt.savefig(
    "figures/top10_candidates.png"
)

# Show figure
plt.show()

print()
print("Top 10 figure saved successfully.")

# Create histogram
# WHY: Shows how predicted overpotentials are distributed across all virtual catalysts
plt.figure(figsize=(8, 5))

plt.hist(
    ranked["Predicted_Overpotential"],
    bins=20
)

plt.xlabel("Predicted Overpotential (mV)")
plt.ylabel("Number of Catalysts")
plt.title("Distribution of Predicted Catalyst Performance")

plt.savefig(
    "figures/predicted_overpotential_distribution.png"
)

plt.show()

print("Prediction distribution figure saved successfully.")