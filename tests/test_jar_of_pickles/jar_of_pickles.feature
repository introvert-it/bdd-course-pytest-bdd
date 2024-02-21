Feature: Jar of pickles

  Scenario: Spinning the lid should allow to open the jar of pickles
    Given user has 2 closed jar(s) of pickles
    And user grabs jar number 1
    When user spins the lid
    And the lid loosens up
    Then user should be able to take the lid off
    And jar of pickles number 1 should be opened
    But jar of pickles number 2 should be closed

  Scenario: Spinning the lid should allow to open the jar of pickles - duplicate with Pytest-like test
    Given user has 2 closed jar(s) of pickles
    And user grabs jar number 1
    When user spins the lid
    And the lid loosens up
    Then user should be able to take the lid off
    And jar of pickles number 1 should be opened
    But jar of pickles number 2 should be closed

  Scenario Outline: Spinning the lid should allow to open given jar of pickles with multiple jars available
    Given user has <number_of_jars> closed jar(s) of pickles
    And user grabs jar number <jar_to_open>
    When user spins the lid
    And the lid loosens up
    Then user should be able to take the lid off
    And jar of pickles number <jar_to_open> should be opened

  Examples:
    |   number_of_jars   |  jar_to_open |
    |       10           |        1     |
    |       10           |        5     |
    |       10           |        10    |
    |       100          |        99    |

  Scenario Outline: Spinning the lid should allow to open multiple jars of pickles
    Given user has <number_of_jars> closed jar(s) of pickles
    When user grabs jars number <jars_list>
    And user spins the lid
    And the lid loosens up
    Then user should be able to take the lids off all the jars
    And jars <jars_list> should be opened

  Examples:
    |   number_of_jars   |  jars_list      |
    |       10           |  [2, 5, 10]     |