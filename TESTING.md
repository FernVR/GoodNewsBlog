# Testing 
Back to [README.md](README.md) file.

# Contents 
- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [Javascript](#javascript)
    - [Python](#python)

- [Python Unit Testing](#python-unit-testing)

- [Automated Testing](#automated-testing)

- [Manual Testing](#manual-testing)
    - [Home Page](#home-page)
    - [About Page](#about-page)
    - [Profile Page](#profile-page)
    - [Sign up/ Sign In/ Sign Out Pages](#sign-up-sign-in-sign-out-pages)
    - [Update/ Delete Profile Page](#update-delete-profile-page)

- [User Story Testing](#user-story-testing)
    - [Developer User Stories](#developer-user-stories)
    - [Visitor User Stories](#visitor-user-stories)
    - [Registered User Stories](#resgistered-user-stories)
    - [Admin User Stories](#admin-user-stories)

- [UI](#ui)

- [Bugs](#bugs)

- [Browser Compatibility](#browser-compatibility)

- [Lighthouse Test Result](#lighthouse-test-result)

## Code Validation
### HTML 
I used [The W3C Markup Validation Service](https://validator.w3.org/) to validate all HTML pages by inputting the source code into the direct input field, these were my results:

| Page | Result | Notes | Result Screenshot |
| ------------ | ------------ | ------------ | ------------ |
| Home | Pass | No errors | <details><summary>Home</summary><img src="docs/testing-md/validations/html-val-home.png"></details> |
| Post Detail | Pass | No errors | <details><summary>Post Detail</summary><img src="docs/testing-md/validations/html-val-post-detail.png"></details> |
| About | Pass | No errors | <details><summary>About</summary><img src="docs/testing-md/validations/html-val-about.png"></details> |
| User Profile | Pass | The errors caused by SummerNote Widget. Removed Widget and tested, no errors were returned. | <details><summary>Profile Errors</summary><img src="docs/testing-md/validations/html-val-profile-page.png"></details><details><summary>Profile Errors </summary><img src="docs/testing-md/validations/html-val-profile-page-1.png"></details><details><summary>Profile Errors</summary><img src="docs/testing-md/validations/html-val-profile-page-3.png"></details> |
| Update Profile | Pass | No errors | <details><summary>Profile Update</summary><img src="docs/testing-md/validations/html-val-update.png"></details> |
| Delete Profile | Pass | No errors | <details><summary>Delete Profile</summary><img src="docs/testing-md/validations/html-val-delete.png"></details> |
| Register/Sign Up | Pass | Errors are are related to built in Django form template  | <details><summary>Sign Up Error</summary><img src="docs/testing-md/validations/html-val-signup-error.png"></details><details><summary>Sign Up</summary><img src="docs/testing-md/validations/html-val-signup.png"></details> |
| Sign In/Sign Out | Pass | No errors | <details><summary>Sign In</summary><img src="docs/testing-md/validations/html-val-login.png"></details><details><summary>Sign Out</summary><img src="docs/testing-md/validations/html-val-logout.png"></details> |

### CSS
I used [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate my style.css file, I got these results:

| Test | Result | Notes | Result Screenshot |
| ------------ | ------------ | ------------ | ------------ |
| style.css | Pass | Recieved 5 warnings (screenshot included) | <details><summary>Result</summary><img src="docs/testing-md/validations/css-validator-result.png"></details><details><summary>CSS Warnings</summary><img src="docs/testing-md/validations/css-validator-warnings.png"></details> |


### Javascript
I used [JSHint](https://jshint.com/) to validate my style.css file, I got these results:

| Test File | Result | Notes | Result Screenshot |
| ------------ | ------------ | ------------ | ------------ |
| comments.js | Pass | No errors - Warnings listed in screenshot | <details><summary>Comment Warnings</summary><img src="docs/testing-md/validations/js-val-comment-js.png"></details><details><summary>Comment Warnings</summary><img src="docs/testing-md/validations/js-val-comment-js-1.png"></details> |
| summernote-init.js | Pass | No errors - warnings listed in screenshot | <details><summary>Summernote Warnings</summary><img src="docs/testing-md/validations/js-val-summernote.png"></details>


### Python
I used [The CI Python Linter](https://pep8ci.herokuapp.com/) to validate my python files, I got these results:

| Test File | Result | Notes | Result Screenshot |
| ------------ | ------------ | ------------ | ------------ |
| blog/views.py | Pass | No errors | <details><summary>blog/views.py</summary><img src="docs/testing-md/validations/py-val-blog-views.png"></details> |
| blog/urls.py | Pass | No errors | <details><summary>blog/urls.py</summary><img src="docs/testing-md/validations/py-val-blog-urls.png"></details> |
| blog/test_views.py | Pass | No errors | <details><summary>blog/test_views.py</summary><img src="docs/testing-md/validations/py-val-blog-test-views.png"></details> |
| blog/test_forms.py | Pass | No errors | <details><summary>blog/test_forms.py</summary><img src="docs/testing-md/validations/py-val-blog-test-forms.png"></details> |
| blog/forms.py | Pass | No errors | <details><summary>blog/forms.py</summary><img src="docs/testing-md/validations/py-val-blog-forms.png"></details> |
| blog/models.py | Pass | No errors | <details><summary>blog/models.py</summary><img src="docs/testing-md/validations/py-val-blog-models.png"></details> |
| blog/apps.py | Pass | No errors | <details><summary>blog/apps.py</summary><img src="docs/testing-md/validations/py-val-blog-apps.png"></details> |
| blog/admin.py | Pass | No errors | <details><summary>blog/admin.py</summary><img src="docs/testing-md/validations/py-val-blog-admin.png"></details> |
| about/views.py | Pass | No errors | <details><summary>about/views.py</summary><img src="docs/testing-md/validations/py-val-about-views.png"></details> |
| about/test_views.py | Pass | No errors | <details><summary>about/test_views.py</summary><img src="docs/testing-md/validations/py-val-blog-test-views.png"></details> |
| about/test_forms.py | Pass | No errors | <details><summary>about/test_forms.py</summary><img src="docs/testing-md/validations/py-val-about-test-forms.png"></details> |
| about/models.py | Pass | No errors | <details><summary>about/models.py</summary><img src="docs/testing-md/validations/py-val-about-models.png"></details> |
| about/admin.py | Pass | No errors | <details><summary>about/admin.py</summary><img src="docs/testing-md/validations/py-val-about-admin.png"></details> |



## Python Unit Testing
Results for testing report can be found in [test_report.txt](test_report.txt) which I generated using the 'python manage.py test -v 2 > test_report.txt' command in the terminal.
(screenshot of python unittest in terminal)

### Automated Testing
screenshot of test results for automated testing. Testing functions can be found in these files:
[Blog/Test Forms](blog/test_forms.py)
[Blog/ Test Views](blog/test_views.py)
[About/ Test Forms](about/test_forms.py)
[About/ Test Views](about/test_views.py)

(screenshot of test results from terminal)

## Manual Testing
Create a different grid for each title, rows are individual items to test, cols are : 'test case' , 'action', 'acceptance criteria', 'result'
### Home Page
#### Links and Buttons 
#### Display and Images 
#### Responsive Design Grid 

### Post Detail Page
#### Links and Buttons 
#### Display and Images 
#### Responsive Design Grid 

### About Page
#### Links and Buttons 
#### Display and Images 
#### Responsive Design Grid 

### Profile Page
- Links and Buttons 
- Display and Images 
- Responsive Design Grid 

### Sign Up/ Sign In/ Sign Out Pages
#### Links and Buttons 
#### Display and Images 
#### Responsive Design Grid 

### Update/ Delete Profile Page
#### Links and Buttons 
#### Display and Images 
#### Responsive Design Grid 

## User Story Testing

(Grid with link to each user story, acceptance criteria results, notes)
### Visitor User Stories
""
### Resgistered User Stories
""
### Admin User Stories
""
## UI 
(include issue with all UI issues included, list attempted fixes)

## Bugs
(Similar to user story grid, add bug issues documented in project and add acceptance criteria results, any notes.)

## Browser Compatibility
(screenshot of grid with compatibilaty results for safari, chrome, firefox on laptop, ipad pro and iphone pro -- use pages app)

## Lighthouse Test Result
screenshots of all results 
- Home Page
- Contact Page
- Profile Page
