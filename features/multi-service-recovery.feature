Feature: Multi-Service Chaos Recovery
  As a developer, I want to ensure that multiple services recover properly after chaos
  So that the system is robust in real-world scenarios.

  Scenario: Test partition and recovery for three services
    Given a distributed system with services "Service X" and "Service Y"
    And a distributed system with service "Service Z"
    When a network partition is introduced between "Service X" and "Service Y"
    And 400ms latency is added to "Service Z" with 50ms jitter
    Then the system should recover after the partition is removed
    And "Service Z" should remain operational
    