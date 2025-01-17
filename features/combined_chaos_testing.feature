Feature: Combined Chaos Scenarios
  As a developer, I want to test the system under multiple chaos conditions
  So that I can identify any unexpected interactions.

  Scenario: Simulate network partition and latency simultaneously
    Given a distributed system with services "Service A" and "Service B"
    When a network partition is introduced between "Service A" and "Service B"
    And 300ms latency is added to "Service B" with 50ms jitter
    Then the system should recover after the partition is removed
    And "Service B" should remain operational