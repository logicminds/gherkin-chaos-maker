import unittest
import os
import json
from behave.__main__ import main as behave_main


class TestBehaveContentGeneration(unittest.TestCase):
    def setUp(self):
        """
        Set up output directory for testing.
        """
        self.output_dir = "output"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    # def tearDown(self):
    #     """
    #     Clean up after tests by removing generated files.
    #     """
    #     for file in os.listdir(self.output_dir):
    #         os.remove(os.path.join(self.output_dir, file))
    #     os.rmdir(self.output_dir)

    def test_eris_experiment_generation(self):
        """
        Run Behave scenarios and validate the eris_experiment file content.
        """
        # Run Behave programmatically
        result = behave_main("features/combined_chaos_testing.feature")

        # Check that Behave ran successfully
        self.assertEqual(result, 0, "Behave execution failed")

        # Validate the generated file
        feature_file_name = "combined_chaos_scenarios.json"
        file_path = os.path.join(self.output_dir, feature_file_name)

        self.assertTrue(
            os.path.exists(file_path), f"Expected file {file_path} not found"
        )

        # Load and verify the file content
        with open(file_path, "r") as f:
            data = json.load(f)

        fixture_file = os.path.join(
            os.path.dirname(__file__), "fixtures", feature_file_name
        )

        with open(fixture_file, "r") as f:
            expected_structure = json.load(f)

        self.assertEqual(
            data,
            expected_structure,
            "Generated content does not match expected structure",
        )


if __name__ == "__main__":
    unittest.main()
