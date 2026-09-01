# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
from pathlib import Path
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "solar.csv"

# Load the latest version
df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "nasa/solar-eclipses",
    file_path,
)
output_path = Path(__file__).resolve().parent.parent / "data" / "solar.csv"
df.to_csv(output_path, index=False)
print(f"Wrote {len(df)} rows to {output_path}")