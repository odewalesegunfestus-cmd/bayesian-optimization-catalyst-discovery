# Import pandas
import pandas as pd

# Import GPR
from sklearn.gaussian_process import GaussianProcessRegressor

# Load training dataset
data = pd.read_csv("data/catalyst_data.csv")

# Define features
X = data[
    [
        "Ni_fraction",
        "Co_fraction",
        "Fe_fraction"
    ]
]

# Define target
y = data["Overpotential_mV"]

# Train GPR model
gpr = GaussianProcessRegressor(
    normalize_y=True,
    random_state=42
)

gpr.fit(X, y)

# Load virtual catalyst search space
search_space = pd.read_csv("results/search_space.csv")

# Predict overpotential and uncertainty
prediction, uncertainty = gpr.predict(
    search_space,
    return_std=True
)

# Add results to search space
search_space["Predicted_Overpotential"] = prediction
search_space["Uncertainty"] = uncertainty

# Save predictions
search_space.to_csv(
    "results/predicted_virtual_catalysts.csv",
    index=False
)

print()
print("FIRST 10 PREDICTED VIRTUAL CATALYSTS")
print(search_space.head(10))

print()
print("Predicted virtual catalysts saved successfully.")