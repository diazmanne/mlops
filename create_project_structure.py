import os
import argparse
import subprocess

def create_folders(base_path):
    folder_structure = {
        "data": [],
        "models": [],
        "notebooks": ["01_data_preparation.ipynb"],
        "src": ["__init__.py", "data.py", "features.py", "models.py", "utils.py"],
    }

    for folder, files in folder_structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            open(file_path, 'a').close()
            print(f"Created file: {file_path}")

    # Print the folder structure using tree command
    print("\nFolder structure created:")
    subprocess.run(["tree", base_path])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a specific folder structure for a project.")
    parser.add_argument("base_path", type=str, help="The base path where the folder structure will be created.")
    args = parser.parse_args()

    create_folders(args.base_path)

