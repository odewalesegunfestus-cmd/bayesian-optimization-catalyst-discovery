# Import pandas
import pandas as pd

# Load predicted virtual catalysts
predictions = pd.read_csv(
    "results/predicted_virtual_catalysts.csv"
)

# Rank by predicted overpotential
# WHY: Lower overpotential means better catalyst
ranked_by_prediction = predictions.sort_values(
    by="Predicted_Overpotential",
    ascending=True
)

# Create EI-like score
# WHY: Reward low overpotential and high uncertainty
predictions["EI_score"] = (
    -predictions["Predicted_Overpotential"]
    + predictions["Uncertainty"]
)

# Rank by EI score
# WHY: Higher EI score means better next experiment
ranked_by_ei = predictions.sort_values(
    by="EI_score",
    ascending=False
)

# Save results
ranked_by_prediction.to_csv(
    "results/ranked_by_prediction.csv",
    index=False
)

ranked_by_ei.to_csv(
    "results/ranked_by_ei.csv",
    index=False
)

print()
print("TOP 10 BY PREDICTED OVERPOTENTIAL")
print(ranked_by_prediction.head(10))

print()
print("TOP 10 BY EI SCORE")
print(ranked_by_ei.head(10))

print()
print("Ranking completed successfully.")