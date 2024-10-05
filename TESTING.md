# Testing 
Back to [README.md](README.md) file.

![Main Image - I am Responsive screenshot](docs/i-am-responsive-goodnews.png)

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

<details><summary>Python Unittest Result</summary> <img src="docs/testing-md/py-unittest-screenshot.png"></details>


### Automated Testing
Testing functions can be found in these files:
[Blog/Test Forms](blog/test_forms.py)
[Blog/ Test Views](blog/test_views.py)
[About/ Test Forms](about/test_forms.py)
[About/ Test Views](about/test_views.py)

<details><summary>Automated testing</summary> <img src="docs/testing-md/automated-test-results.png"></details>

## Manual Testing
Extensive Manual Testing was carried out during the duration of this project. I tried to test each feature/link upon creating them, I have also included screenshots of the testing grids I created.
### Home Page
<details><summary>Links and Buttons </summary> <img src="docs/testing-md/man-testing-home-links.jpg"></details>

<details><summary>Display and Images</summary> <img src="docs/testing-md/man-testing-home-display.jpg"></details>

<details><summary>Responsive Design Grid </summary> <img src="docs/testing-md/man-testing-home-responsive.jpg"></details>


### Post Detail Page
<details><summary>Links and Buttons </summary> <img src="docs/testing-md/man-testing-post-detail-links.jpg"></details>

<details><summary>Display and Images</summary> <img src="docs/testing-md/man-testing-post-detail-display.jpg"></details>

<details><summary>Responsive Design Grid </summary> <img src="docs/testing-md/man-testing-post-detail-responsive.jpg"></details>

### About Page
<details><summary>Links and Buttons </summary> <img src="docs/testing-md/man-testing-about-links-buttons.jpg"></details>

<details><summary>Display and Images</summary> <img src="docs/testing-md/man-testing-about-display.jpg"></details>

<details><summary>Responsive Design Grid </summary> <img src="docs/testing-md/man-testing-about-responsive.jpg"></details>


### Profile Page
<details><summary>Links and Buttons </summary> <img src="docs/testing-md/man-testing-profile-links.jpg"></details>

<details><summary>Display and Images</summary> <img src="docs/testing-md/man-testing-profile-display.jpg"></details>

<details><summary>Responsive Design Grid </summary> <img src="docs/testing-md/man-testing-profile-responsive.jpg"></details>

### Sign Up/ Sign In/ Sign Out Pages
<details><summary>Links and Buttons </summary> <img src="docs/testing-md/man-testing-sign-up-links-buttons.jpg"></details>

* Display / Images : No images used on this section. Display has no errors.

<details><summary>Responsive Design Grid </summary> <img src="docs/testing-md/man-testing-signup-responsive.jpg"></details>

### Update/ Delete Profile Page
<details><summary>Links and Buttons </summary> <img src="docs/testing-md/man-testing-post-detail-links.jpg"></details>

* Display / Images : No images used on this section. Display has no errors.

<details><summary>Responsive Design Grid </summary> <img src="docs/testing-md/man-testing-update-delete-responsive.jpg"></details>

## User Story Testing

### Admin User Stories

| User Story | Acceptance Criteria Complete | Screenshot/Notes |
| ------------ | ------------ | ------------ | 
| [Managing Comments](https://github.com/FernVR/GoodNewsBlog/issues/9) | Pass | <details><summary>Comments Admin Page</summary><img src="docs/testing-md/user-story-screenshots/comments-admin.png"></details> |
| [Managing Posts](https://github.com/FernVR/GoodNewsBlog/issues/6) | Pass | <details><summary>Posts Admin Page</summary><img src="docs/testing-md/user-story-screenshots/posts-admin.png"></details> |

### Visitor User Stories

| User Story | Acceptance Criteria Complete | Screenshot/Notes |
| ------------ | ------------ | ------------ | 
| [Sign Up](https://github.com/FernVR/GoodNewsBlog/issues/12) | Pass | <details><summary>Sign Up Link</summary><img src="docs/testing-md/user-story-screenshots/sign-up-nav.png"></details><details><summary>Sign Up Form</summary><img src="docs/testing-md/user-story-screenshots/sign-up-form.png"></details> |
| [Scroll Blog Posts](https://github.com/FernVR/GoodNewsBlog/issues/10) | Pass | <details><summary>Post List - Home Page</summary><img src="docs/testing-md/user-story-screenshots/post-list-home.png"></details> |
| [View Blog Posts](https://github.com/FernVR/GoodNewsBlog/issues/23) | Pass | <details><summary>Post Detail Page</summary><img src="docs/testing-md/user-story-screenshots/post-detail.png"></details> |
| [Visit About Page](https://github.com/FernVR/GoodNewsBlog/issues/7) | Pass | <details><summary>About Page</summary><img src="docs/testing-md/user-story-screenshots/about-page.png"></details><details><summary>Feedback Form</summary><img src="docs/testing-md/user-story-screenshots/feedback-form.png"></details> - Includes Feedback form |
| [View Comments](https://github.com/FernVR/GoodNewsBlog/issues/45) | Pass | <details><summary>Comments- Logged Out</summary><img src="docs/testing-md/user-story-screenshots/view-comments.png"></details> |

### Resgistered User Stories

| User Story | Acceptance Criteria Complete | Screenshot/Notes |
| ------------ | ------------ | ------------ | 
| [User Profile Page](https://github.com/FernVR/GoodNewsBlog/issues/26) | Pass | <details><summary>Profile Page</summary><img src="docs/testing-md/user-story-screenshots/profile-page.png"></details> |
| [Adding Comments](https://github.com/FernVR/GoodNewsBlog/issues/17) | Pass | <details><summary>Add Comment Form</summary><img src="docs/testing-md/user-story-screenshots/adding-comments.png"></details><details><summary>Edit Comment</summary><img src="docs/testing-md/user-story-screenshots/updating-comment.png"></details><details><summary>Delete Comment</summary><img src="docs/testing-md/user-story-screenshots/delete-comment.png"></details> |
| [User Add Posts](https://github.com/FernVR/GoodNewsBlog/issues/18) | Pass | <details><summary>Add Post Form</summary><img src="docs/testing-md/user-story-screenshots/add-post-form.png"></details> | 
| [User Delete Profile](https://github.com/FernVR/GoodNewsBlog/issues/52) | Pass |<details><summary>Update Profile Details</summary><img src="docs/testing-md/user-story-screenshots/update-profile.png"></details> <details><summary>Delete Profile Message</summary><img src="docs/testing-md/user-story-screenshots/profile-delete.png"></details> |


## Bugs

| Bug/Issue | Resolved/Unresolved | Notes |
| ------------ | ------------ | ------------ | 
| [About Page - Nav and Footer UI Issue](https://github.com/FernVR/GoodNewsBlog/issues/29) | Resolved | added boostrap styles to all sections to ensure no content pushes the nav and footer. |
| [Comment Count](https://github.com/FernVR/GoodNewsBlog/issues/28) | Resolved | Fixed using connotate and Q |
| [User/ Profile](https://github.com/FernVR/GoodNewsBlog/issues/43) | Resolved | added signals to create profile page when new user is created |
| [Text field on user post form](https://github.com/FernVR/GoodNewsBlog/issues/44) | Resolved | Added add post section only to users with larger screen resolutions - would like to include a small/medium size text field later, so feature is available to all users on different devices - documented in Future Features section of [README.md](README.md) |
| [Comment Section - responsive design](https://github.com/FernVR/GoodNewsBlog/issues/47) | Resolved/Partially | User information on comment section and comments are still not spaced correctly, larger comments squash too close together. This is because of the display flex on both of those sections, but I kept it as it was because it looks correct on medium/larger screens. 
| [User Profile Page - UI Issue](https://github.com/FernVR/GoodNewsBlog/issues/50) | Unresolved | <details><summary>Profile Page UI Bug</summary> <img src=""></details> Couldn't fix the push on nav and footer content after attempting to with adjusting all boostrap classes and styling on each section, I think the issue is coming from the post list section, but I can't figure out exactly. |
| [Contact app/Django Crispy Form](https://github.com/FernVR/GoodNewsBlog/issues/27) | Unresolved | I deleted the contact app as I was only going to use it for the form, I included the form within the About section instead. |
| [Bug: UI Problems - User Profile Page section](https://github.com/FernVR/GoodNewsBlog/issues/51) | Unresolved | Tried to fix this in lots of different ways and couldn't find a suitable solution in time. ![Screenshot](docs/testing-md/placeholder-img-bug-2.png) | 


## Browser Compatibility
<details><summary>Browser Compatibility Grid </summary> <img src="docs/testing-md/browser-compatibility.jpg"></details>

## Lighthouse Test Result
 I generated a Google Lighthouse report and got this result:

 ![Lighthouse Result](docs/testing-md/goodnews-lightouse-home.png)

 The score for Best Practises was a lot lower than I'd hoped, I tried to use the report to solve the issues but I wasn't able to find an adequate solution. I would definitely be trying to improve this score in future.

<details><summary>Lighthouse Best Practises </summary> <img src="docs/testing-md/goodnews-lighthouse-bp.png"></details>

