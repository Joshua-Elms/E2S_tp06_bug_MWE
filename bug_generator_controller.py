from earth2studio.data import CDS, ARCO, GFS
from earth2studio.models.px import SFNO, Pangu6, GraphCastOperational, FuXi
print("All earth2studio imports successful.")
import subprocess

models = dict(
    fuxi=FuXi,
    graphcast=GraphCastOperational,
    pangu=Pangu6,
    sfno=SFNO,
)
data_sources = dict(
    cds=CDS,
    arco=ARCO,
    gfs=GFS,
)
"""Main function to run tests."""
output_file = "test_results.txt"
for model_name in models:
    for data_source_name in data_sources:
        subprocess.run(["python", "-c", f"from bug_generator_utils import test_model; test_model('{model_name}', '{data_source_name}', '{output_file}')"], check=True)

print("All tests completed. Results written to", output_file)
print("Results:\n")
with open(output_file, "r") as f:
    for line in f:
        print(" ", line.strip())