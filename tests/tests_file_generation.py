import unittest
import os
import json
from features.environment import save_experiment_to_file


class TestFileGeneration(unittest.TestCase):
    def setUp(self):
        """
        Create a test directory and dummy experiment data.
        """
        self.output_dir = "test_output"
        self.experiment_data = {
            "version": "1.0",
            "name": "Test Experiment",
            "description": "This is a test.",
            "phases": [],
        }

    def tearDown(self):
        """
        Clean up the test directory after each test.
        """
        if os.path.exists(self.output_dir):
            for file in os.listdir(self.output_dir):
                os.remove(os.path.join(self.output_dir, file))
            os.rmdir(self.output_dir)

    def test_file_generation(self):
        """
        Test that the experiment file is correctly generated.
        """
        feature_name = "Test Feature"
        file_path = save_experiment_to_file(
            self.experiment_data, feature_name, self.output_dir
        )

        # Check if the file exists
        self.assertTrue(os.path.exists(file_path))

        # Verify file contents
        with open(file_path, "r") as f:
            data = json.load(f)
            self.assertEqual(data, self.experiment_data)

    def test_file_name_formatting(self):
        """
        Test that the file name is formatted correctly.
        """
        feature_name = "My Cool Feature"
        file_path = save_experiment_to_file(
            self.experiment_data, feature_name, self.output_dir
        )

        expected_file_name = "my_cool_feature.json"
        self.assertTrue(file_path.endswith(expected_file_name))


if __name__ == "__main__":
    unittest.main()
