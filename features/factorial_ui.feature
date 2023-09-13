Feature: Compute factorial using UI


Background:
  Given I am using the greatest factorial calculator

@ui
Scenario Outline: Factorial UI

  Given I enter <number> on the field
  When I click Calculate! button
  Then I see 'The factorial of <number> is: <result>'

 Examples: Numbers to calculate
   | number | result                |
   | 10     | 3628800               |
   | 170    | 7.257415615307999e+306|
   | 171    | Infinity              |

