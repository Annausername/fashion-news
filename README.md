# Fashionista News #

Fashionista News is a Reddit-like news site where users can interact with articles on various fashion-related topics. Users can browse through a list of news, view article details, like articles, upvote or downvote articles, and post comments. This project aims to provide a platform for fashion enthusiasts to stay updated with the latest news and trends in the fashion industry.

[Live Site](https://fashionista.herokuapp.com/)

## Contents
- [User Experiences](#user-experience)
  - [User Stories](#user-stories)
  - [Agile Methodology](#agile-methodology)
  - [Database](#database)
- [Features](#features)
  - [Existing Features](#existing-features)
- [Technologies](#technologies)
  - [Languages & Frameworks](#languages-and-frameworks)
  - [Other](#other)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Database](#database)
  - [Heroku](#heroku)
  - [Cloudinary](#cloudinary)
- [Credits](#credits)

## **User Experiences**
### **User Stories**

As a user, I should be able to:
  - View news list
  - View an article
  - Registrer an account
  - View comments
  - Comment on an article
  - View likes
  - Like / Unlike
  - See time/date of posting
  - Upvote/downvote a particular article
[Back to top](#contents)

### **Agile Methodology**

This project was developed using Agile methodology, following the principles and practices outlined in Agile to manage and develop the project. ![Project board](https://github.com/Annausername/fashion-news/blob/main/media/project.png)
[Back to top](#contents)

## **Features**
### **Existing Features**
### Navbar

![The navigation bar](https://github.com/Annausername/fashion-news/blob/main/media/navbar.png)

Provides easy access to different sections of the website. It includes the following options:

- Home: Clicking on the "Home" link will take you to the main page of Fashionista, where you can browse articles and engage with the community.
- Register: If you are new to Fashionista, you can click on the "Register" link to create a new account. Registration allows you to participate in discussions, upvote/downvote articles, and more.
- Login: If you already have an account, click on the "Login" link to access your account. Logging in enables you to post comments, submit articles, and interact with other users.
- Logout: If you are currently logged in, the "Logout" option will be available in the navigation bar. Clicking on "Logout" will securely sign you out of your account.
[Back to top](#contents)

### News List
News list: Users can view a list of news/articles on the home page, sorted by uvoting.![view](https://github.com/Annausername/fashion-news/blob/main/media/listings.png)
### Article View (non registered)
Users can click on an article to view its details, including the title, content, author and date posted. ![view](https://github.com/Annausername/fashion-news/blob/main/media/article%20view%20n%3Ar.png)
### Article View (registered)
Users can click on an article to view its details, including the title, content, author, date posted, likes and comments.
## Upvote/Downvote
Users can upvote or downvote articles on the main page to express their opinion on the article's quality or relevance.
## Likes
Logged-in users can like articles to show their appreciation or agreement
## Comments
Logged-in users can post comments on articles to share their thoughts, ask questions, or engage in discussions.
# Admin View (comments)
Admin can delete users comments if they wish to remove them. ![view](https://github.com/Annausername/fashion-news/blob/main/media/delete.png)
### Login/Register
User will be shown a simple form requesting them to input a username and password. If the user doesn't have account they have the option to create one.![view](https://github.com/Annausername/fashion-news/blob/main/media/login.png)
### SignUp
The user requested to enter a username, email and password.
### LogOut
To Sign out user will be asked to confirm an action. ![view](https://github.com/Annausername/fashion-news/blob/main/media/logout.png)
[Back to top](#contents)

The UI/UX (User Interface/User Experience) is an essential aspect of any project, including Fashionista, and it still requires major input.

## **Technologies**
### **Languages and Frameworks**
  - [Python](https://www.python.org/)
  - [Django](https://www.djangoproject.com/)
  - [Bootstrap](https://getbootstrap.com/)
  - [HTML5](https://en.wikipedia.org/wiki/HTML5)
  - [CSS3](https://en.wikipedia.org/wiki/CSS)

### **Other**
  - [ElephantSQL](https://www.elephantsql.com/) was used as the Postgres, database system
  - [Font Awesome](https://fontawesome.com/) was used to provide icons throughout the app
  - [Heroku](https://www.heroku.com/home?) was used to host my deployed project
  - [Auto PEP8](https://pypi.org/project/autopep8/) was used at the end to try and tidy up some of my python files

[Back to top](#contents)

## **Testing**

## Manual Testing

### Nav Bar
  - Ability to select 'Home' nav link - PASS
  - If user not logged in, display 'Log In' nav link - PASS
  - Abilty to select 'Log In' nav link - PASS
  - If user logged in, display Logout instead - PASS
  - Ability to 'SignUp' nav link - PASS
  - Ability to select 'Log Out' nav link - PASS

### Home Page
  - Ability to select and choose an acticle from the list - PASS
  - Ability to change page using the pagination buttons - PASS
  - Ability to Upvote/Downvote posts - PASS
  - Ability to view an article - PASS

### PC Detail Page
  - If user is logged in, show ability to leave comment, othervise don't show - PASS
  - If user is logged in, show ability to like article, othervise don't show - PASS
  - If admin is logged in, show delete comment button, othervise don't show - PASS

### Log In Page
  - SignIn works properly - PASS

### Register Page
  - SignUp works properly - PASS

### Article 
  - If non logged in user gets to this page, display error message with login redirect button - PASS
  - If valid data is entered, allow form to be posted - PASS
  - If invalid data is entered, don't allow form to be posted - PASS
  - Only upload images that are JPEG or PNG - PASS
  - All fields are mandatory - PASS

### Like
  - If user is logged, comment function works - PASS

### Comment
  - If user is logged, comment function works, send a request to admin for approvel and redirects to home page. UUser sees an alert that the comment needs moderation  - PASS

### Delete 
  - If admin is logged, delete comment function works and redirects to home page - PASS


## Validation 

### HTML Validation
### Home Page 
  - No errors apart from some styling elements. This appears to be related to font awesome and nothing related to my created code.

### CSS Validation

Running my style.css file through the validator returned no errors.

### Python Validation
To note I have not put all python files.

## Models

# Article Model

Test creating an article: Ensures that an article can be created with the required fields (title, content, author).

# Comment Model

Test creating a comment: Ensures that a comment can be created with the required fields (article, name, email, content).
![model](https://github.com/Annausername/fashion-news/blob/main/media/test%20models.png)
## Views

# ArticleDetail View

Test retrieving article detail: Ensures that the article detail page can be accessed successfully. It checks for the correct HTTP response status code (200), the correct template used (article_detail.html), and the presence of the article's title and the content of the first comment.

# CommentDeleteView

Test deleting a comment: Ensures that a comment can be deleted successfully. It checks for the correct HTTP response status code (302) after deleting a comment and verifies that the comment no longer exists in the database.
The tests help verify the functionality and behavior of the models and views in the Fashionista application. They ensure that the data is being stored correctly and that the views are rendering the expected output. Running the test suite provides confidence in the reliability of the application and helps identify any issues or regressions.
![views](https://github.com/Annausername/fashion-news/blob/main/media/test%20views.png)
## Device Testing

Using Google Developer Tools, I mimicked mobile phones in the browser to test for scaling and to ensure all data was displayed clearly. During my testing everything behaved as intended and all images were very clear, all containers scaled down to fit corectly. All functionality was still working with no issues.

The Fashionista project includes a suite of tests to ensure the stability and functionality of the application. However, the testing coverage is an area that requires more attention and enhancement from a developert perspective. 

[Back to top](#contents)

## **Deployment**
### **Database**
To create a managed Postgres database go to ElephantSQL and Sign Up / Login.
  - Click on 'Create new instance'
  - Name your database, choose the 'Tiny Turtle' plan and click 'Select Region'

Database name:

  - Choose your region and then create the database. instance.
  - In the instances page, click the name of your chosen database.
  - In the details section of the following page copy the postgres url.

Database details:

You can now use this URL when linking the database to the project repository.

[Back to top](#contents)

### **Heroku**

  - Sign Up / Login to Heroku
  - Create a new app from the Heroku dashboard
  - Give the app a unique name and enter the region of operation then click 'create app'.
  - From your newly created app choose the settings tab and navigate to 'Reveal Config Vars'.
  - Paste the ElephantSQL Database url into the DATABASE_URL environment variable.

Heroku config vars:

  - Create an env.py file in the root directory of your Django project (at the same directory level as requirements.txt and manage.py). Once created add the filename to .gitignore as it stores sensitive info.
  - Paste the ElephantSQL url for the DATABASE_URL value.
  - Add the following libraries to the settings.py file: Import Path from pathlib, dj_database_url and os.
  - Create a secret key to replace the insecure SECRET_KEY variable in the settings.py file. Link the secure key in env.py to the settings.py SECRET_KEY variable with the following code: SECRET_KEY =os.environ.get('SECRET_KEY')
  - Add your secret key to HEROKU Config Vars.
  - Link the DATABASES value to the env.py file with the following code: DATABASES = { 'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }
  - You can now migrate the app models to the new database using the command: "python3 manage.py makemigrations" then Python3 manage.py migrate.

[Back to top](#contents)

## **Cloudinary**

  - Signup/Signin to Cloudinary
  - Copy the 'cloudinary url' from your account dashboard and paste it as the CLOUDINARY_URL value in env.py.
  - Add the CLOUDINARY_URL to the Config Vars in Heroku.
  - Also Add the DISABLE_COLLECTSTATIC Key with the value of 1
  - Change the static file settings in Django by altering the following.
  - The STATIC_URL
  - STATICFILES_STORAGE
  - STATICFILES_DIRS
  - STATIC_ROOT
  - MEDIA URL
  - DEFAULT_FILE_STORAGE

The STATIC section of settings.py should resemble the following image:

  - Change the TEMPLATES 'DIRS' Setting in Settings.py to [TEMPLATES_DIR] TEMPLATES configuration for the project should resemble the following image:

  - Back nearer the top of the settings.py file add the Setting TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
  - Create 3 new folders for static files, media files and HTML templates. (At the same directory level as requirements.txt and manage.py.)
  - Create a Procfile(capital P) and add the following: web: gunicorn NAME_OF_THE_APP_GOES_HERE.wsgi
  - Add the app name and herokuapp.com to the list of ALLOWED_HOSTS.
  - Add and commit the changes to GitHub.
  - Remove DISABLE_COLLECTSTATIC from Heroku Config Vars
  - Deploy via the 'Deploy Main Branch' button in the Deployment page of HEROKU.
  - If you receive an success message, you can click the link provided to view the app in the web browser.

[Back to top](#contents)

## **Credits**
- This project references a lot on the [Therefore I Think Blog](https://github.com/Code-Institute-Solutions/Django3blog) project of the code institute.
- During the work on the project I browsed a lot of resources like [StackOverflow](https://stackoverflow.com/), but no actual code was taken from there.
- CodeInstitute Slack channel.
### Media Sources
- All media files were taken from a [Pexels](https://www.pexels.com/), stock photography and stock footage provider.
