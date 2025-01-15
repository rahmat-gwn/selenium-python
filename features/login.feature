Feature: Login Functionality
    Sebagai pengguna
    Saya ingin dapat login ke sistem
    Agar saya dapat mengakses fitur yang dilindungi

Scenario: Valid Login
    Given User is on the login page
    When User enters valid username "user_valid" and valid password "password_valid"
    And User clicks the login button
    Then User should be logged in successfully and see "Selamat datang"

Scenario: Invalid Login - Wrong Username
    Given User is on the login page
    When User enters invalid username "user_invalid" and valid password "password_valid"
    And User clicks the login button
    Then User should see an error message "Username atau password salah"

Scenario: Invalid Login - Wrong Password
    Given User is on the login page
    When User enters valid username "user_valid" and invalid password "password_invalid"
    And User clicks the login button
    Then User should see an error message "Username atau password salah"