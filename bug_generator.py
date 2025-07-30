from earth2studio.data import CDS
from earth2studio.models.px import SFNO, Pangu6, GraphCastOperational, FuXi
import earth2studio.run as run
from earth2studio.io import XarrayBackend
print("All earth2studio imports successful.")
from dotenv import load_dotenv
load_dotenv()
print("Environment variables loaded.")

models = dict(
    fuxi=FuXi,
    graphcast=GraphCastOperational,
    pangu=Pangu6,
    sfno=SFNO,
)

for model_name, model in models.items():
    print(f"MODEL: {model_name.upper()}")
    try:
        dummy_io = XarrayBackend()
        CDS_data_source = CDS()
        print("\tLoading model...")
        package = model.load_default_package()
        model = model.load_model(package)
        print("\tModel loaded.")
        print("\tRunning inference...")
        output = run.deterministic(["2024-01-01"], 1, model, CDS_data_source, dummy_io)
        del model
        print("\tInference complete.")
    except Exception as e:
        print(f"\tError encountered while running {model_name} model: {e}")
    print("\n") 