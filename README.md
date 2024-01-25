# Hi-find

## Setup & Run Server
  - Clone the  project
  - Create the virtual environment for the django project in the clone folder using the following command
  - `python -m venv myvirtual`
  - Activate the virtural  environment using the following commands
  - `cd myvirtual`
  - `Scripts\Activate`
  - After that, exist from that folderInstall the required libraries with the following commands
  - `cd ..`
  - `pip install -r requirements.txt`
  ### Set up database
  - Create database named `lost_portal` at your MySql Database
  - And configure the username and password of MySql at hi_find\settings.py file

  - Run the following command to start the server
  - `python manage.py makemigrations`
  - `python manage.py migrate`
  - `python manage.py runserver`

### Setup & Run Socket Server
  - Open new terminal window
  - Change dir to socket folder `cd socket`
  - `npm i`
  - `npm start`


## Project folder Info
  - *hi-find* folder is the main project file for the whole project. Need to configure settings.py and urls.py in this folder.
  - *home* folder is the app for home page. 
  - *login* folder is the app for login page.
  - *signup* folder is the app for Signup page.
  - *posts* folder is the app for posts pages. Posts details, Posts Lists, Posts Update and Delete Pages with be set under this folder.

### For the html files, check the templates folder under each App folder and for the images places in the Static folder --> static/images.

## Created Database Info
  - `lostUser (user_id,username,email,password,gender,create_at)`



