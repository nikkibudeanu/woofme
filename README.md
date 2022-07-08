
<h1 align=center> Woofme</h1>


<p align=center> Are you a dog owner? <br/> Are you a dog lover? <br/> Find out what people say about different breeds, find your perfect breed or share feedback on your dog's breed on our website. Woofme is a place where you can add a review and do a research on other breeds! <br/> Woofme is a place for dog lovers. <br/> Woofme is a place for (almost) EVERYONE!

 </p>

<img src="">


 ## Project Purpose


## User Experience



### User Stories

1. As a user, I would like to be able to ...
1.1. Register on Woofme using username, email and password. 
1.2 Be able to view all the reviews added on Woofme.
1.3 Be able to view detailed reviews about different breeds.
1.4 Search for a breed or breed group on the navigation bar.

2. As a logged user, I would like to be able to...
2.1 Create breed reviews adding:
+ Breed name
+ Breed Group
+ A review on the breed
+ Adaptability, trainability, friendliness and health and grooming needs rating. 
+ Overall breed rating
+ Breed image

2.2 Create a new breed if a breed is not in the database.

2.3 Edit and delete a previously added review.

2.4 Check a breed review after added. 


### 1. Strategy

 + **Project Goal**
  
  Create a project that allows its users to evaluate their favorite pets and read reviews on other pets adaptability, 
  friendliness, health and grooming needs as well as trainability. 


### 2. Scope 

As a project owner, I would like to create :

* a simple, straightforward website with intuitive UX experience.
* clear and easy navigation for the user through each of woofme's features.
* a visually appealing website on all devices.


### 3. Structure

* Navbar is fixed on top to facilitate Woofme uers to navigate easily and pleasantly. 
* Edit, Delete and Add review buttons present on all forms to enable users to have an intuitive and smooth experience.
* Layout is clear to allow woofme users navigate intuitively.
* Login/Logout/Register options present on the navbar to ensure that Woofme users are able to perform each of the actions easily.


### 4. Skeleton

The wireframes are created with Figma.

* Home page wireframe


* Add review page wireframe


* Review list page wireframe


* Search page wireframe


* Review page wireframe


* Login/Logout/Register pages wireframe

### 5. Surface



* Colors
<img src="media/color_palette.jpg">


* Font selection



## Functional Scope 
**Woofme Flowchart**

<img height= "700" src="media/readme/">

**Agile Methodology**
All functionality and development of the project was managed using GitHub project tool and personal notes.

<details>
<summary>All sprints are described here.</summary>

Test cases were linked with every User story presented above, and can be found in TESTING.md(TESTING.md) - Automated testing section. 

* Sprint 1

  + Setup Django 
  + Heroku Deployment 
  + Create User Stories in Github


* Sprint 2
  + Create User Profile
  + Create Register Page
  + Create Login Page 
  

* Sprint 3
  + Create all models


* Sprint 4
  + Create Add Review feature 
  + Upload an image on breed review
  + Add rating breed feature


* Sprint 5

  + Create a search by breed



* Sprint 6

  + Create final tests


</details>


## Release History
<img width= "800" src="">

## Features

### **Navbar** 

+ Fixed Navbar allow the user easy access to all pages. 

1. Login and  Register User buttons are present on the navbar if the user is not logged. 

<img width="800" src="media/readme/">

2. Logout and Rate a breed buttons are present if the user is logged. 

<img width="800" src="media/readme/">

3. Breed reviews and search breed by name/ group are present to all users (logged or not).

4. User can use the search bar to look for a favorite breed

    i. Dropdown menu with all breed groups.

    ii. Find a breed by its name.

     <img width="400" src="media/readme/">

    iii. Users will get feedback if there are no reviews on the breed they are looking for and will be encouraged to rate that breed.

    iv. If the review is found, the user will be redirected to the review page to see all details on the searched breed.

5. On smaller devices, the navigation bar is going to be a hamburger menu to ensure a better navigation.

  <img width="400" src="media/readme/">

### **Breed review list page**

1. Users will access a list of all reviews.

  <img width="800" src="media/readme/">

2. Each review card contains breed name, group, image, the preview of the review , each criteria level, breed rating, author and publication date. 

* The entire card is a link to the breed review  page.

<img height="50%" src="media/readme/">

* When breed name and breed group are long, should apply a truncate class. The full names can be seen on the breed review page.

### **Breed  review  page** 

1. On this page, users can access the entire content for a review. 

<img width="800" src="media/readme/">

  1.1 When an old user is accessing the previously created review, he will have two buttons available : edit and delete.
   
<img width="200" src="media/readme/">


### **Edit Review Page** 

1. Users can change a review field using this page.
2. The back button will bring the user to the previous page without changes on review. 

<img width="800" src="media/readme/">

### **Delete Review Page** 

1. When clicking on the delete button, the users will be redirected to the delete review page where they can get rid of the review.

<img width="800" src="media/readme/">

### **Search breed group, breed Pages** 

1. After searching a breed using the search bar or the dropdown menu, the users will be redirected to these pages.

  1.1 Breed group search example:

  <img width="800"  src="media/readme/">

  1.2 Breed search example: 

  <img height="800" src="media/readme/">

2. If no review is available, users will get feedback. 



## Future Features
* Single sign-on using social media.



## Languages Used

Python , Javascript, CSS


## Frameworks, Libraries & Programs Used

+ Figma:
+ Font Awesome: 
+ Git: 
+ GitHub: 
+ Google Fonts: 
+ Django: 
+ Pexels:
+ Multi Device Website Mockup Generator: Used to generate mockup image.
+ getcssscan.com for the boxshadow.



## Testing and Code validation 
All code validation and tests details can be found [here](TESTING.md).

## Project Bugs and Solutions:


## Deployment 

This App is deployed using Heroku.

## FAQ about the uptime script

# Credits

### Work based on other code

# Acknowledgements
