# Testing

During the code development, tests were performed to make sure the functions/views/URLs are running as expected.

Please see below all tests.

## Code Validation Testing

## Auto-tests

### **WOOFME** 
Manual and automated testing was conducted on woofme app, users app as well as the project URLs.

<p><img src="media/readme/unittests/overall.png"></p>

========================================================================================

### **Users App** 
Almost all functions on the users' app were tested automatically using unit tests. Manual testing was performed on the other tests to ensure there are no errors.

* Overall
<p><img src="media/readme/unittests/overall-users.png"></p>


* Forms
<p><img src="media/readme/unittests/forms-users.png"></p>



* Views
<p><img src="media/readme/unittests/views-users.png"></p>


<details>
<summary>
User Stories covered by tests.

+  "User Story:Account Login/Logout"
+  "User Story:Account Registration"

</summary>

| test_forms| test_views |  
|    ---    |  ---       |
| SignupFormTest() |  TestRegister() |  
| SignUpFormTestInvalid()|TestLogin()|
||TestLogout()|   | 

</details>
========================================================================================

### **woofme_app** 

*  Unittests Overall
<p><img src="media/readme/unittests/overall-woofmeapp.png"></p>

* Views 
<p><img src="media/readme/unittests/views-woofmeapp.png"></p>

  * Forms 
<p><img src="media/readme/unittests/forms-woofmeapp.png"></p>

 * Urls 
<p><img src="media/readme/unittests/urls-woofmeapp.png"></p>

 * Models

<p><img src="media/readme/unittests/models-woofmeapp.png"></p>

<details>
<summary> User stories covered by tests: 

+ "User Story: search breed."
+ "User Story: view breeds list."
+ "User Story: add a dog breed + review + image"
+ "User Story: create breed review"
+ "User Story: Open a breed details page."
+ "User Story: See a list of breed groups using a dropdown menu."
+ "User Story: Edit/Delete previously created review."
</summary>

| test_models| test_views |  test_forms
|    ---    |  ---       | ---
| BreedReviewTestCase() | AddReviewViewTest()  |  CreateBreedFormTest()
| BreedTestCase()      |BreedRatingView()|
| BreedGroupTestCase()  |ReviewPageViewTests()|
|            |EditReviewViewTests()|
|            |SuccessfulEditReviewViewTests()|
</details>


<details><summary>
Tests covering User Story :

+ "User Story: Search breed."

</summary>

| test_views |   
|  ---       |    
| TestSearchBreedView() |  

</details>

### **Overall Test on plataform** 


To check that I covered all automated tests, I have used coverage tools. See the results below:

<p><img src="media/readme/unittests/covreport.png"></p>


+ **woofme**

Overall report for the woofme project.

Uncovered lines in the settings file were tested manually. In the woofme/views file, the uncovered lines are those related to error handling pages (400, 404, 500). They were tested manually with no errors.


<p><img src="media/readme/unittests/covreport-woofme.png"></p>


+ **woofme_app**

Uncovered lines on woofme app are present only on the views file. They are related to DeleteReviewViews and EditReviewViews. Manual tests were performed to ensure no error was detected.

<p><img src="media/readme/unittests/covreport-woofmeapp.png"></p>

  
+ **users app**

On the users' app, there are also some uncovered lines on the views that were tested manually. 

<p><img src="media/readme/unittests/covreport-users.png"></p>

   
   ## Integration Test Case


+ On this project, the Incremental Testing method was used.

 An incremental testing approach was used for this project to find issues at an early stage and solve them. Please find these tests for each feature below.



### **Navbar**

| Test Case Id | Description | RESULT|
|:----:|:----:|:----:|
| 1 | Click Breed Reviews' navbar button| To be directed to the breed Reviews Page|
| 2 | Click the Logo navbar button| To be directed to the home page|
| 3 | Add a breed name (present on DB) on the left field and search | To be directed to the search breed page with a short intro to the review.|
| 4 | Add a breed name (not present on DB) on left field search | To be directed to the search breed page with feedback on lack of reviews and button to add review page.|
| 5 | Click login's navbar button | To be directed to the Login Page|
| 6 | A logged User clicks logout's navbar button | To be logged out and directed to the Home Page|

### **Login**

| Test Case Id | Description | RESULT|
|:----:|:----:|:----:|
| 1 | Enter login credentials and click on the Login button| To be directed to the home page and success message.|
| 2 | Enter invalid data in the login form and click the login button.| Error message!|

### **Register**

| Test | Description | RESULT|
|:----:|:----:|:----:|
| 1 | Enter data and click register button| Directed home page + success alert message.|
| 2 | Enter invalid data in the register form.| ERROR MESSAGE.|



### **Reviews Card**

| Test | Description | RESULT|
|:----:|:----:|:----:|
| 1 | Click in a breed review card on the review list| To be directed to the breed page view. |
| 2 | Click on the Edit button on the card| To be redirected to the edit review page|
| 3 | Click on the Delete button on the card| To be redirected to confirm deletion page|

### **Footer** 

| Test | Description | RESULT|
|:----:|:----:|:----:|
| 1 | Click on the social media buttons| To be directed to social media pages. |




### **Buttons**

The following buttons were tested:


| Button | RESULT|
|:----:|:----:|
| Next pagination button| To be direct to the next review page|
| Last pagination button| To be direct to the last review page|
| First button| To be direct to the first review page|
| Previous button| To be direct to the previous review page|
| Go Back button on the edit review page| To be direct to the previous navigated page|
| Back to Reviews button on the detailed review page| To be direct to the breed reviews navigated page|
| Edit button on the edit review page| To be direct to the breed page navigated page and be presented with a new edited review|
| Star in rating breed or edit breed page | Populate breed rating field on review form|
| Adaptability/trainability/friendliness/health and grooming needs dropdown button on add breed rate or edited breed page | Displayed with all criteria choices (1-5)|
| Upload image button on add breed rate or edit breed page. | Opens a directory in your device.|




## Python (PEP8) Validation

###  **Woofme App** 

<p float="left">
        <img src="media/readme/pep8/woofme-settings.png" width="400" height="200" />
        <img src="media/readme/pep8/woofme-test-views.png" width="400" height="200" />
        <img src="media/readme/pep8/woofme-urls.png" width="400" height="200" />
        <img src="media/readme/pep8/woofme-views.png" width="400" height="200" />

</p>

+ Error in settings file - line too long - link. 


###  **Users App** 

<p float="left">
        <img src="media/readme/pep8/users-forms.png" width="400" height="200" />
        <img src="media/readme/pep8/woofme-test-forms.png" width="400" height="200" />
        <img src="media/readme/pep8/users-test-views.png" width="400" height="200" />
        <img src="media/readme/pep8/users-urls.png" width="400" height="200" />
        <img src="media/readme/pep8/users-views.png" width="400" height="200" />
</p>

### **Woofme_app App** 


<p float="left">
        <img src="media/readme/pep8/app-admin.png" width="400" height="200" />
        <img src="media/readme/pep8/app-apps.png" width="400" height="200" />
        <img src="media/readme/pep8/app-forms.png" width="400" height="200" />
        <img src="media/readme/pep8/app-models.png" width="400" height="200" />
        <img src="media/readme/pep8/app-test-forms.png" width="400" height="200" />
        <img src="media/readme/pep8/app-test-models.png" width="400" height="200" />
        <img src="media/readme/pep8/app-test-urls.png" width="400" height="200" />
        <img src="media/readme/pep8/app-test-views.png" width="400" height="200" />
        <img src="media/readme/pep8/app-urls.png" width="400" height="200" />
        <img src="media/readme/pep8/app-views.png" width="400" height="200" />

+ line too long errors related to cloudinary links.

</p>


## HTML Code Validation
HTML Validation not perfomed as W3 is not configured for django HTML files and a lot of invalid errors were showing up. However, I manually checked them and made sure formatting is performed and no errors are showing. 

## CSS Code Validation

<p float="left">
        <img src="media/readme/validation/css-validation.png" width="40%" />
</p>

## JavaScript Code Validation

### **add review js** 

<p float="left">
        <img src="media/readme/validation/add-review-js-valid.png" width="40%" />
</p>

### **script js** 


<p float="left">
        <img src="media/readme/validation/script-js-valid.png" width="40%" />
</p>


### **toollip js** 

Error explanation- Bootstrap is defined on the base file. 

<p float="left">
        <img src="media/readme/validation/toolip-js-valid.png" width="40%" />
</p>


## Exploratory Testing
========================================================================================

### Initial User Testing 

The test user was my husband. I held a test session with him and here are the results! 

1. **Home page**


  + The user suggested a different background image to have more contrast.
  + The user required a button on the home page that redirects to the review list(not only the navbar breed reviews button). This is to increase interaction on the body of the home page.


2. **Navbar**

   + The colors on the navbar are not contrasting with the background color of the home page which creates a visual illusion. 

3. **Search breed and review list** 
   + Too much information on review cards, you can see everything without opening the review page. 

4. **Extra tips**

   + The user proposed to integrate a search by breed group function into the website. 


### **Response to the user experience test:**

+ All user feedback was taken into account and incorporated except 4. as it is planned to be a future feature.


### Final User Testing 

For this test, I have created a checklist for the user which included tests for all features of the pages. Please see the results below: 


<p float="left">
        <img src="media/readme/unittests/user-test.png" width="40%" />
</p>


### **Response to the user test:**

+ All bugs were fixed before submission and suggestions were implemented.

## Manual Testing
========================================================================================

### Desktop
* Google Chrome: everything is working well. All features are functioning, no problems performing all steps of CRUD. 

* Safari: no issues found here in final check.  



### Mobile

* Tested with iPhone 11 PRO and Woofme works well without errors.


### WAVE Accesibility validation

**Home page analysis**

<p float="left">
        <img src="media/readme/validation/home-wave.png" width="40%" />
</p>


**Breed Reviews analysis**

<p float="left">
        <img src="media/readme/validation/reviewlist-wave.png" width="40%" />
</p>

**Add review Page analysis**

<p float="left">
        <img src="media/readme/validation/addreview-wave.png" width="40%" />
</p>

**Login Page analysis**

<p float="left">
        <img src="media/readme/validation/login-wave.png" width="40%" />
</p>

**Register Page  analysis**

<p float="left">
        <img src="media/readme/validation/register-wave.png" width="40%" />
</p>

### Lighthouse validation

**Home page Lighthouse analysis**

<p float="left">
        <img src="media/readme/validation/home-lighthouse.png" width="40%" />
</p>

**Breed Reviews Lighthouse analysis**

<p float="left">
        <img src="media/readme/validation/reviewlist-lighthouse.png" width="40%" />
</p>

**Add review Page Lighthouse analysis**

<p float="left">
        <img src="media/readme/validation/addreview-lighthouse.png" width="40%" />
</p>


**Login Page Lighthouse analysis**

<p float="left">
        <img src="media/readme/validation/login-lighthouse.png" width="40%" />
</p>

**Register Page Lighthouse analysis**

<p float="left">
        <img src="media/readme/validation/register-lighthouse.png" width="40%" />
</p>


# Unfixed bugs

* No unfixed bugs present, only future features that I have tried but not managed to finish: breed groups drop-down menu. Not implemented as decided to do it at a late stage in my project development. Very eager to implement it as soon as my project is graded.
