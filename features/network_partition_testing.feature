Feature: Network Partition Resilience
  As a developer, I want to test how the system behaves when services are partitioned
  So that I can ensure it recovers gracefully.

  Scenario: Simulate a network partition between Service A and Service B
    Given a distributed system with services "Service A" and "Service B"
    When a network partition is introduced between "Service A" and "Service B"
    Then the system should recover after the partition is removed

  Scenario: Simulate a network partition between Service C and Service D
    Given a distributed system with services "Service C" and "Service D"
    When a network partition is introduced between "Service C" and "Service D"
    Then the system should recover after the partition is removed
    