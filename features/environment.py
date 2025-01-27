import os
import json

def before_feature(context, feature):
    """
    Initialize the eris_experiment object before each feature.
    """
    context.eris_experiment = {
        "version": "1.0",
        "name": "",
        "description": "",
        "metadata": {"region": "na", "cluster": "default", "businesses": "bankofmemes"},
        "parameters": {
            "business1": "bankofmemes",
            "env": "test",
            "cluster": "default",
            "region": "na",
            "deployment_id": "1234",
            "bearer_token": "Bearer sdfksdafasdf",
        },
        "phases": [],
    }


def save_experiment_to_file(experiment, feature_name, output_dir="output"):
    """
    Save the given experiment object to a JSON file named after the feature.
    """

    os.makedirs(output_dir, exist_ok=True)
    file_name = f"{feature_name.replace(' ', '_').lower()}.json"
    file_path = os.path.join(output_dir, file_name)

    with open(file_path, "w") as f:
        json.dump(experiment, f, indent=2)

    return file_path  # Return the file path for verification


def after_feature(context, feature):
    if hasattr(context, "eris_experiment"):
        file_path = save_experiment_to_file(context.eris_experiment, feature.name)
        print(f"Eris experiment saved to {file_path}")
    else:
        print("No eris_experiment found in feature.")
