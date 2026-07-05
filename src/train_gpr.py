# Import pandas
import pandas as pd

# Load dataset
data = pd.read_csv(
    "data/catalyst_data.csv"
)

# Show first rows
print()
print("CATALYST DATA")

print(
    data.head()
)

# Show dataset shape
print()
print("DATASET SHAPE")

print(
    data.shape
)

# Define features
# WHY: These are the catalyst variables used to predict overpotential
X = data[
    [
        "Ni_fraction",
        "Co_fraction",
        "Fe_fraction"
    ]
]

# Define target
# WHY: This is the catalyst performance value we want to predict
y = data[
    "Overpotential_mV"
]

print()
print("FEATURES")
print(X.head())

print()
print("TARGET")
print(y.head())

# Import GPR model
# WHY: GPR predicts overpotential and gives uncertainty
from sklearn.gaussian_process import GaussianProcessRegressor

# Create GPR model
# WHY: normalize_y helps the model learn the overpotential scale correctly
gpr = GaussianProcessRegressor(
    normalize_y=True,
    random_state=42
)

# Train GPR model
# WHY: Teach the model using catalyst features and overpotential values
gpr.fit(
    X,
    y
)

print()
print("GPR model trained successfully.")

# Create new catalyst
# WHY: Test the trained model on a catalyst composition
new_catalyst = pd.DataFrame(
    [
        [0.70, 0.20, 0.10]
    ],
    columns=[
        "Ni_fraction",
        "Co_fraction",
        "Fe_fraction"
    ]
)

# Predict overpotential and uncertainty
prediction, uncertainty = gpr.predict(
    new_catalyst,
    return_std=True
)

print()
print("PREDICTED OVERPOTENTIAL")
print(prediction)

print()
print("UNCERTAINTY")
print(uncertainty)