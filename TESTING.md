# Testing

During the code development, tests were perfomed to make sure the functions/views/urls are running as expected.

Please see below all tests.

## Code Validation Testing

## Automated tests

### **WOOFME** 
Manual and automated testing were conducted on woofme app, users app as well as the project urls.

<p><img src="media/readme/"></p>

========================================================================================

### **Users App** 
All functions on the users' app were tested automatically using unit tests.

* Overall
<p><img src="media/readme/unittests/"></p>


* Forms
<p><img src="media/readme/unittests/"></p>



* Views
<p><img src="media/readme/unittests/"></p>


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
<p><img src="media/readme/unittests/"></p>

* Views 
<p><img src="media/readme/unittests/"></p>

  * Forms 
<p><img src="media/readme/unittests/"></p>

 * Urls 
<p><img src="media/readme/unittests/"></p>

 * Models

<p><img src="media/readme/unittests/"></p>

<details>
<summary> User stories covered by tests: 

+ "User Story: search breed."
+ "User Story : view breeds list."
+ "User Story: add a dog breed + review + image"
+ "User Story: create breed review"
+ "User Story: Open a breed details page."
+ "User Story: See a list of breed groups using a dropdown menu."
+ "User Story: Edit/Delete previously created review."
</summary>

| test_models| test_views |  test_forms
|    ---    |  ---       | ---
| breedReviewTestCase() | AddReviewViewTest()|  | BreedGroupTestCase()|
| BreedTestCase()|BreedRatingView()|
|            |ReviewPageViewTests()|
|            |EditReviewViewTests()|
|            |SuccessfulEditReviewViewTests()||            |TestSearchBreedView()|
</details>


### **Overal Test on plataform** 


In order to check that I covered all automated tests, I have used coverage tools.

<p><img src="media/readme/unittests/"></p>


+ **woofme/views.py**



+ **woofme_app/views.py**

  
+ **woofme/settings.py**

   
   ## Integration Test Case


+ On this project, the Incremental Testing method was used.

 Integrated units were checked after the developer finished writing code for every new feature. This approach was used to find defects early and because it was easy to find the cause of the defect thanks to a step-by-step examination. 

+ The integration tests were divided by features/pages and its described below: 


### **Navbar**

| Test Case Id | Description | Expect result|
|:----:|:----:|:----:|
| 1 | Click B Reviews' navbar button| To be directed to the breed Reviews Page|
| 2 | Click login's navbar button | To be directed to the Login Page|
| 3 | Click in one of breed groups' options on the dropdown menu| To be directed to the breed group category page with a piece of information about my search|
| 4 | Add a breed name (present on DB) on left field and click search | To be directed to the breed category page with a piece of information about my search|
| 5 | Add a breed name (not present on DB) on left field and click search | To be directed to the breed category page with information about the unexistence of records about this breed|
| 6 | A logged User click logout's navbar button | To be logged out and directed to the Home Page|

### **Login**

| Test Case Id | Description | Expect result|
|:----:|:----:|:----:|
| 1 | Enter login credentials and click on the Login button| To be directed to the home page|
| 2 | Enter invalid login credentials and click on the Login button| To be presented to an error message for each invalid field|

### **Register**

| Test Case Id | Description | Expect result|
|:----:|:----:|:----:|
| 1 | Enter all register data and click on the Sign In button| To be directed to the home page, presented to a success message and already logged in|
| 2 | Enter invalid register data in any field and click on the Login button| To be given to an error message|



### **Reviews Card**

| Test Case Id | Description | Expect result|
|:----:|:----:|:----:|
| 1 | Click in a breed review card| To be directed to the breed detail view 
| 2 | Click on Edit button present on card| To be direct to update review page|
| 3 | Click on Delete button present on card| To be direct to confirm deletion page|

### **Footer** 

| Test Case Id | Description | Expect result|
|:----:|:----:|:----:|
| 1 | Click on the LinkedIn button| To be directed to the developer's LinkedIn page. |
| 2 | Click on the Github button | To be directed to the developer's GitHub page.|



### **Buttons**

| Test Case Id | Description | Expect result|
|:----:|:----:|:----:|
| 1 | Click Next pagination button| To be direct to the next review page|
| 2 | Click Last pagination button| To be direct to the last review page|
| 3 | Click First pagination button| To be direct to the first review page|
| 4 | Click Previous pagination button| To be direct to the previous review page|
| 5 | Click Go Back button on update review page| To be direct to the previous navigated page|
| 5 | Click Back to Reviews button on detail review page| To be direct to the breed reviews navigated page|
| 6 | Click Edit button on edit review page| To be direct to the breed page navigated page and be presented with new updated review|
| 7 | Click on a star in rating breed or update breed page | Populate breed rating field on review form|
| 10 | Click on adaptability/trainability/friendliness/health and grooming needs dropdown button on add breed rate or update breed page | Be presented with all criterias choices (1-5)|
| 12 | Click on browse image button on add breed rate or update breed page | Open your directory to find an image to upload|
| 13 | Check clear on update breed page | Clear image previously uploaded to breed review|
| 14 | Click Review Your breed Now on breed or breed group categories page| To be direct to the add breed review page|
| 15 | Click Login and Review on breed or breed group categories page| To be direct to the login page|


## Python (PEP8) Validation

###  **Woofme App** 

###  **Users App** 

### **Woofme_app App** 


## HTML Code Validation

## CSS Code Validation

## JavaScript Code Validation

### **add_review.js** 

### **script.js** 

### **toollip.js** 


## Exploratory Testing
========================================================================================

### Initial User Testing (Alpha)

A session was held with an test-user. The feedback obtained is listed below:


### **Response to the user experience test:**


## Manual Testing
========================================================================================
### Desktop



### Mobile



### WAVE Accessibility validation

**Home page WAVE analysis**

**Breed Reviews WAVE analysis**

**Add review Page WAVE analysis**

**Edit review Page WAVE analysis**

**Breed Search Page WAVE analysis**

**Breed Search Page (with no reviews) WAVE analysis**


# Unfixed bugs




