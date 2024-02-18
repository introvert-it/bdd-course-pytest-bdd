Feature: Jar of pickles

  @with-pickles
  Scenario: Spinning the lid should allow to open the jar of pickles
    Given user has 2 closed jar(s) of pickles
    And user grabs jar number 1
    When user spins the lid
    And the lid loosens up
    Then user should be able to take the lid off
    And jar of pickles number 1 should be opened
    But jar of pickles number 2 should be closed

  Scenario: Spinning the lid should allow to open the jar of pickles 2
    Given user has 2 closed jar(s) of pickles
    And user grabs jar number 1
    When user spins the lid
    And the lid loosens up
    Then user should be able to take the lid off
    And jar of pickles number 1 should be opened
    But jar of pickles number 2 should be closed

  Scenario: Spinning the lid should allow to open the jar of pickles 3
    Given user has 2 closed jar(s) of pickles
    And user grabs jar number 1
    When user spins the lid
    And the lid loosens up
    Then user should be able to take the lid off
    And jar of pickles number 1 should be opened
    But jar of pickles number 2 should be closed
