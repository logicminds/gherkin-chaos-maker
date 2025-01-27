# Chaos Testing Framework with Behave

This project uses **Behave**, a behavior-driven development (BDD) framework, to test and generate chaos testing experiments in JSON format. The framework includes step definitions, hooks, and tests to ensure the correct generation of chaos experiments.


## Features

- Create **Eris experiments** from Gherkin scenarios.
- Automatically save generated experiments as JSON files.
- Unit tests to validate individual components.
- Integration tests to ensure the entire process works as expected.
- Extensible and developer-friendly structure.


## Setup

### Prerequisites

- Python 3.10 or newer
- `pip` (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/logicminds/gherkin-chaos-maker
   cd gherkin-chaos-maker
   ```

2. Setup the environment
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install requirements
```
pip install -r requirements.txt
```


## Layout 
```
chaos-testing/
├── features/                     # Behave feature files and steps
│   ├── chaos_testing.feature      # Gherkin scenarios
│   ├── steps/
│   │   ├── chaos_testing_steps.py # Step definitions
│   ├── environment.py             # Behave hooks (e.g., after_feature)
├── tests/                        # Unit and integration tests
│   ├── test_file_generation.py    # Unit tests for file generation
│   ├── test_behave_integration.py # Integration tests for Behave scenarios
├── output/                       # Generated JSON files (ignored in `.gitignore`)
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
```

## Example Feature
```gherkin
Feature: Chaos Testing with Behave
  As a developer, I want to generate Eris experiments from Gherkin scenarios
  So that I can test the resilience of my system.

  Scenario: Simulate a network partition between Service A and Service B
    Given a distributed system with services "Service A" and "Service B"
    When a network partition is introduced between "Service A" and "Service B"
    Then the system should recover after the partition is removed

```
## Example output 
```json
{
  "version": "1.0",
  "name": "Chaos Experiment: Service A and Service B",
  "description": "Test resilience of Service A and Service B.",
  "phases": [
    {
      "name": "Chaos Injection",
      "description": "Introduce network partition between Service A and Service B.",
      "steps": [
        {
          "action": "network_partition",
          "description": "Partition Service A from Service B.",
          "input": {
            "target": "Service A",
            "isolate_from": "Service B"
          }
        }
      ]
    }
  ]
}
```

## Development Workflow
1.	Write Scenarios:
Add Gherkin scenarios in .feature files under the features/ directory.
2.	Implement Step Definitions:
Write step definitions in Python files under the features/steps/ directory.
3.	Run Tests:
Use Behave to execute the scenarios and generate JSON files.
4.	Validate Output:
Confirm that the eris_experiment files are correct.
5.	Write Tests:
Add unit and integration tests in the tests/ directory.


## Running Unit Tests

Run unit tests to validate individual components, such as file generation logic:

`python -m unittest discover -s tests`


## Integration Tests
Run integration tests to ensure the entire system works as expected, including Behave scenarios and file generation:
`python tests/tests_behave_integration.py`

## Usage
### generaeting the chaos files
Run the Behave tests to generate chaos experiments:
`behave`

### To run a specific feature:
`behave features/chaos_testing.feature`

### To run a specific scenario:
`behave --name "Simulate a network partition between Service A and Service B"`
