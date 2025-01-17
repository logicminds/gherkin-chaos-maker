import os
import json
from behave import given, when, then

eris_experiment = {
    "version": "1.0",
    "name": "",
    "description": "",
    "phases": []
}
 
@given('a distributed system with services "{serviceA}" and "{serviceB}"')
def step_given_distributed_system_with_two_services(context, serviceA, serviceB):
    context.eris_experiment["name"] = f"Chaos Experiment: {serviceA} and {serviceB}"
    context.eris_experiment["description"] = f"Test resilience of {serviceA} and {serviceB}."



@given('a distributed system with service "{service}"')
def step_given_distributed_system_with_one_service(context, service):
    context.eris_experiment["name"] = f"Chaos Experiment: {service}"
    context.eris_experiment["description"] = f"Test resilience of {service}."



@when('a network partition is introduced between "{serviceA}" and "{serviceB}"')
def step_when_network_partition(context, serviceA, serviceB):
    context.eris_experiment["phases"].append({
        "name": "Chaos Injection",
        "description": f"Introduce network partition between {serviceA} and {serviceB}.",
        "steps": [
            {
                "action": "network_partition",
                "description": f"Partition {serviceA} from {serviceB}.",
                "input": {
                    "target": serviceA,
                    "isolate_from": serviceB
                }
            }
        ]
    })


@when('{latency}ms latency is added to "{service}" with {jitter}ms jitter')
def step_when_latency_added(context, latency, service, jitter):
    context.eris_experiment["phases"].append({
        "name": "Chaos Injection",
        "description": f"Add {latency}ms latency to {service} with {jitter}ms jitter.",
        "steps": [
            {
                "action": "network_latency",
                "description": f"Add {latency}ms latency to {service}.",
                "input": {
                    "target": service,
                    "latency_ms": int(latency),
                    "jitter_ms": int(jitter)
                }
            }
        ]
    })




@then('the system should recover after the partition is removed')
def step_then_recover_from_partition(context):
    context.eris_experiment["phases"].append({
        "name": "Recovery",
        "description": "Remove network partition and verify recovery.",
        "steps": [
            {
                "action": "remove_network_partition",
                "description": "Reconnect all services.",
                "input": {}
            }
        ]
    })




@then('"{service}" should remain operational')
def step_then_service_remains_operational(context, service):
    context.eris_experiment["phases"].append({
        "name": "Observation",
        "description": f"Verify {service} remains operational.",
        "steps": [
            {
                "action": "http",
                "description": f"Check {service} status.",
                "input": {
                    "method": "GET",
                    "url": f"http://{service.lower()}.local/health"
                },
                "expect": {
                    "status": 200,
                    "body_contains": "Operational"
                }
            }
        ]
    })
    

def save_eris_experiment(context, feature, eris_experiment):
    """
    Hook to save the experiment file after each feature.
    """
    output_dir = "output"
    print(feature.name)
    os.makedirs(output_dir, exist_ok=True)
    # Use the feature name for the output file
    feature_name = feature.name.replace(" ", "_").lower()
    file_name = f"{feature_name}.json"
    file_path = os.path.join(output_dir, file_name)

    with open(file_path, "w") as f:
        json.dump(eris_experiment, f, indent=2)

    print(f"Experiment saved to {file_path}")