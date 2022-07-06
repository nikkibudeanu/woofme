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
| BeerReviewTestCase() | AddReviewViewTest()|  | BreedGroupTestCase()|
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

   