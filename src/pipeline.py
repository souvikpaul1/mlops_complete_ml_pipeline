import subprocess
import os

# Define the scripts in the desired execution order
scripts = [
    "data_ingestion.py",
    "data_preprocessing.py",
    "feature_engineering.py",
    "model_building.py",
    "model_evaluation.py"
]

# Get the directory of the current script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

print("Running pipeline in order:\n")

for script in scripts:
    script_path = os.path.join(SCRIPT_DIR, script)
    
    if not os.path.exists(script_path):
        print(f"Script not found: {script}")
        continue

    print(f"--- Running {script} ---")
    result = subprocess.run(["python", script_path], capture_output=True, text=True)

    print(result.stdout)
    if result.stderr:
        print(f"Error in {script}:\n{result.stderr}")

    print(f"--- Finished {script} ---\n")
