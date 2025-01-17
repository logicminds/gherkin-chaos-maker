Feature: Latency Tolerance
  As a developer, I want to test how the system handles increased latency
  So that I can ensure it remains operational.

  Scenario: Add 500ms latency to Service A
    Given a distributed system with service "Service A"
    When 500ms latency is added to "Service A" with 50ms jitter
    Then "Service A" should remain operational

  Scenario: Add 1s latency to Service B
    Given a distributed system with service "Service B"
    When 1000ms latency is added to "Service B" with 100ms jitter
    Then "Service B" should remain operational

  Scenario: Add 2s latency to Service C
    Given a distributed system with service "Service C"
    When 2000ms latency is added to "Service C" with 200ms jitter
    Then "Service C" should remain operational
    
