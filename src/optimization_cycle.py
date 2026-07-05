# Import pandas
import pandas as pd

# Load EI-ranked catalysts
ei_ranked = pd.read_csv(
    "results/ranked_by_ei.csv"
)

# Select best EI candidate
best_candidate = ei_ranked.iloc[0]

print()
print("BEST NEXT CATALYST TO TEST")
print(best_candidate)

# Simulate laboratory result
# WHY: In real research, this value comes from experiment
experimental_overpotential = 198

# Create new experimental row
new_experiment = pd.DataFrame(
    [
        {
            "Catalyst_ID": "BO_1",
            "Ni_fraction": best_candidate["Ni_fraction"],
            "Co_fraction": best_candidate["Co_fraction"],
            "Fe_fraction": best_candidate["Fe_fraction"],
            "Overpotential_mV": experimental_overpotential
        }
    ]
)

# Load original dataset
original_data = pd.read_csv(
    "data/catalyst_data.csv"
)

# Add new experiment to dataset
updated_data = pd.concat(
    [original_data, new_experiment],
    ignore_index=True
)

# Save updated dataset
updated_data.to_csv(
    "results/updated_catalyst_data_after_bo_cycle.csv",
    index=False
)

print()
print("UPDATED DATASET SAVED")
print(updated_data.tail())