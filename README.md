# Django Playground/Health Progress Tracker

Small Django project with 4 currently functioning apps:

1. User Accounts
    * Registration/Login
    * Authentication
    * User Id used as a foreign key for other app data
2. Daily intake tracker
    * Track daily calories and protein intake
    * Data is tied to user account by foreign key, only viewable for logged in user
    * Calculates total for each day and current day
3. TDEE (Total Daily Energy Expenditure) Calculator:
    * Stores biometric data, can be updated
    * Calculates and displays Total Daily Energy Expenditure with corresponding formula
4. Community Post board:
    * View posts from other users
    * Write own posts
    * Edit and Delete functionality for posts, only available for posts authored by current logged in user
## 

I developed this web application for mainly personal use as well as a means to learn about the Django web framework through experimenting. Will occasionally update as I discover more about the framework.




