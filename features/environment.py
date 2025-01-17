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
        "phases": []
    }
    
def after_feature(context, feature):
    """
    Save the eris_experiment object after each feature.
    """
    if hasattr(context, "eris_experiment"):
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        # Use the feature name to name the output file
        feature_name = feature.name.replace(" ", "_").lower()
        file_name = f"{feature_name}.json"
        file_path = os.path.join(output_dir, file_name)

        # Write the eris_experiment to a JSON file
        with open(file_path, "w") as f:
            json.dump(context.eris_experiment, f, indent=2)

        print(f"Eris experiment saved to {file_path}")
    else:
        print("No eris_experiment found in context for this feature.")