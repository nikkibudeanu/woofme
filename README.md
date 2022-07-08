
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


* Add review page wireframe

<img width="500" src="media/readme/wireframes/1.png">



* Review list page wireframe

<img width="500"" src="media/readme/wireframes/2.png">


* Search page wireframe(if breed is on the db)

<img width="500" src="media/readme/wireframes/6.png">

If breed is not on the website, user will get feedback and he will have access to a button which redirects to add review page so he can add the first review for the breed. 


* Review page wireframe

If user is logged in and is looking at a previously added review, he will have the options to delete or edit it. 

<img width="500" src="media/readme/wireframes/5.png">


* Login/Logout/Register pages wireframe

+ Login page:

<img width="500" src="media/readme/wireframes/3.png">

+ Register page:

<img width="500" src="media/readme/wireframes/4.png">


### 5. Surface


* Colors

My color choice was a blue color palette which is very user friendly and appealing. I collected it from icolorpalette.com .

<img width="300" src="media/readme/color_palette.jpg">


* Font selection

Tthe font was chosen with [Google Fonts](https://fonts.google.com/) to be used across the website.

The font is chosen in 2 weights: 300 for the paragraphs and 900 for the headings.

<img width="500" src="media/readme/fonts.png">


## Functional Scope 
**Woofme Flowchart**

<img width="500" src="media/readme/chart.png">

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
  + README file

</details>


## Features

### **Navbar** 

+ Fixed Navbar allow the user easy access to all pages. 

1. Login and  Register User buttons are present on the navbar if the user is not logged. 

<img width="500" src="media/readme/features/nav-desk.png">

* On smaller devices, the navigation bar is going to be a hamburger menu to ensure a better navigation.


<img width="500" src="media/readme/features/nav-mob.png">

2. Logout and Rate a breed buttons are present if the user is logged. 

<img width="500" src="media/readme/features/logout.png">

3. Breed reviews and search breed by name/ group are present to all users (logged or not).

4. User can use the search bar to look for a favorite breed.

    i. Find a breed by its name.

     <img width="500" src="media/readme/features/searched.png">

    ii. Users will get feedback if there are no reviews on the breed they are looking for and will be encouraged to rate that breed.

    iii. If the review is found, the user will be redirected to the review page to see all details on the searched breed.



### **Breed review list page**

1. Users will access a list of all reviews.

  <img width="500" src="media/readme/features/list.png">

2. Each review card contains breed name, group, image, the preview of the review , each criteria level, breed rating, author and publication date. 

* The entire card is a link to the breed review  page.

<img height="50%" src="media/readme/features/review-page.png">

### **Breed  review  page** 

1. On this page, users can access the entire content for a review. 

  1.1 When an old user is accessing the previously created review, he will have two buttons available : edit and delete.
   
<img width="500" src="media/readme/features/edit-delete.png">


### **Edit Review Page** 

1. Users can change a review field using this page.
2. The back button will bring the user to the previous page without changes on review. 

<img width="500" src="media/readme/features/edit.png">

### **Delete Review Page** 

1. When clicking on the delete button, the users will be redirected to the delete review page where they can get rid of the review.

<img width="600" src="media/readme/features/delete.png">

### **Search breed Page** 

1. After searching a breed using the search bar, the users will be redirected to a results page. 

2. If no review is available, users will get feedback. 

<img width="600" src="media/readme/features/no-review.png">

### **Login Page** 


### **Register Page** 


## Future Features
* Single sign-on using social media.
* Serch by breed-group.



## Languages Used

Python , Javascript, CSS


## Frameworks, Libraries & Programs Used

+ Canva: used for building wireframes.
+ Font Awesome: used for icons.
+ Git: used for development.
+ GitHub: used for user stories.
+ Google Fonts: used for fonts links.
+ Django: language.
+ Pexels: used for all pictures.
+ Multi Device Website Mockup Generator: Used to generate mockup image.
+ getcssscan.com: used for the box shadow on review cards. 



## Testing and Code validation 
All code validation and tests details can be found [here](TESTING.md).

## Project Bugs and Solutions:

| Bugs              | Solutions |
| ---               | --------- |
| When deploying, the website css and database was failing on Heroku. | Debug Update and transfering all data to postgres. A model did not have a slug as per old migrations.
| Rating criterias on review page and search breed pages were not updating visually. | Typeerror on these pages (review instead of object). 
| Delete and Edit buttons were not displaying. | TypeError on delete and edit pages links.
| Search breed page not working.| Old variable name for "created_at" field - TypeError.

## Deployment 

This App is deployed using Heroku.

<details>
<summary>Deployment steps </summary>
 
 1. Ensure all apps are listed on requirements.txt. 
 
Command:  ` pip3 freeze > requirements.txt`. 
 
 2. Setting up your Heroku
 
  2.1 Login to heroku and enter your details: 
  command: ` heroku login -i` 

    <img src="media/readme/deployment/heroku_login.png">

    
    2.3 Get your app name from heroku.
    command: `heroku apps`
    

    2.4 Set the heroku remote. 
    ommand: `heroku git:remote -a woofmeapp`
    

    2.5. Add, commit and push to github
    command: `git add . && git commit -m "Deploy to Heroku via CLI"`

    2.6. 5. Push to both github and heroku
    `command: git push origin main`
    `command: git push heroku main`
       
</details>

## FAQ about the uptime script

# Credits

## Media

+ All pictures and images used in this project are from [Pexels](https://pexels.com).

### Work based on other code

# Acknowledgements
