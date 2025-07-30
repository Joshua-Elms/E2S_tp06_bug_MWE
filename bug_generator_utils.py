from earth2studio.data import CDS, ARCO, GFS
from earth2studio.models.px import SFNO, Pangu6, GraphCastOperational, FuXi
import earth2studio.run as run
from earth2studio.io import XarrayBackend
print("All earth2studio imports successful.")
from dotenv import load_dotenv
load_dotenv()
print("Environment variables loaded.")
import traceback
import torch

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

def test_model(model_name: str, data_source_name: str, output_file: str):
    """Test a model with a specific data source. Output written to file"""
    torch.cuda.empty_cache()  # Clear CUDA cache to avoid memory issues
    model = models[model_name]
    data_source = data_sources[data_source_name]()
    dummy_io = XarrayBackend()
    print(f"---- Testing {model_name} with {data_source_name} data source ----")
    try:
        package = model.load_default_package()
        model_instance = model.load_model(package)
        print("Model loaded.")
        print("Running inference...")
        output = run.deterministic(["2023-01-01"], 1, model_instance, data_source, dummy_io)
        print("---- Inference passed ----\n")
        passed = True, None

    except Exception as e:
        print(f"Error encountered while running {model_name} model w/ {data_source_name} data source:\n{traceback.format_exc()}")
        print("---- Inference failed ----\n")
        passed = False, e
        
    with open(output_file, "a") as f:
        result = "Passed" if passed[0] else f"Failed w/ error \"{passed[1]}\""
        f.write(f"{model_name}-{data_source_name}: {result}\n")

def main():
    """Main function to run tests."""
    results = {}
    for model_name in models:
        for data_source_name in data_sources:
            result = test_model(model_name, data_source_name)
            results[f"{model_name}_{data_source_name}"] = result
    print("Test results:")
    for key, value in results.items():
        print(f"{key}: {'Passed' if value else 'Failed'}")
        
if __name__ == "__main__":
    main()
    print("Script executed successfully.")