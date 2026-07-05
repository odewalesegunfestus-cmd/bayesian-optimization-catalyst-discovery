# Import pandas
# WHY: Create and save catalyst search-space table
import pandas as pd

# Create empty list
# WHY: Store valid Ni-Co-Fe catalyst compositions
catalysts = []

# Generate Ni-Co-Fe compositions
# WHY: Create virtual catalysts where Ni + Co + Fe = 1
for ni in range(5, 96, 5):

    for co in range(5, 96, 5):

        # Calculate Fe
        # WHY: Fe completes the total composition to 100%
        fe = 100 - ni - co

        # Keep only valid catalysts
        # WHY: Fe must be positive and at least 5%
        if fe >= 5:

            catalysts.append(
                [
                    ni / 100,
                    co / 100,
                    fe / 100
                ]
            )

# Convert list to DataFrame
search_space = pd.DataFrame(
    catalysts,
    columns=[
        "Ni_fraction",
        "Co_fraction",
        "Fe_fraction"
    ]
)

# Save search space
search_space.to_csv(
    "results/search_space.csv",
    index=False
)

print()
print("SEARCH SPACE CREATED")
print(search_space.head())

print()
print("TOTAL VIRTUAL CATALYSTS")
print(len(search_space))

print()
print("Search space saved successfully.")