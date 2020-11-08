Feature: cellar app
  
  As a hobbyist
  I want to make my work easier
  By taking calculations of my head
  
  Scenario Outline: app stores recipes
    Given I found recipe I want to save for future calculations
    And I have copied the amount of ingredients
    And optional target volume
    And optional target amount of alcohol
    When I confirm my input
    Then recipe can be looked up
    And if <posible?>, return <what> target amount in liters
    And recipe can be corrected
    And recipe can be deleted
    
    Examples:
      |posible?|what|
      | possible|calculated|
      | not possible|place to input|
    
  
  Scenario: app performs calculations
    Given amount of ingredients
    And name of end product
    When I confirm my input
    Then app will return suggestions according to recipe
    And I will be able to correct these suggestions
    And save them
    
    
    
Feature: app uses calendar
  
  As a hobbyist
  I want to remember when to do things in the future
  By putting them in calendar
  
  Scenario Outline: app can add action to recipe
    Given recipe requires performing additional action next day or later
    And I had input estmated time since <when>
    And I can optionally add ingredients and amount
    When I confirm adding action
    Then action is added to the recipe
    And I can add another action
    And the data is saved
    And I can update or delete action
    
    Examples:
      |when|
      | preceeding action|
      | start|
    
    
  Scenario: Adding ingredients within the action
    Given I have chosen to add ingredient within an action
    And I choose one of the ingredients of recipe
    And I input the amount
    And the amount is not higher than recipe total or sum of the used ingredients
    When I finish typing the data
    Then I can add another ingredient
    And I can save the action
    And I can delete the ingredient input
    
    
  Scenario: action can be optional 
    
  Scenario: action is added to calendar, when I start doing the recipe
    Given I have selected a recipe with action
    And I have input all the needed data
    When I start performing the recipe
    Then action is added to the calendar