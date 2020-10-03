                                 shortsummary


#About ShortSummary

Shotsummary is a book summary keeping website. The solo purpose of this website is to store summaries
of the books and save lot of time to going through whole books. 

# Technology Used
Django, Html5, Css, Bootstrap

# Structural description of the project
Contains two directories:
1) book_app --> is the app in which all important views, models, templates are coded.
2) naveen_book_project -->  is the main project directory

# INSTALLATION GUIDE FOR UBUNTU 16+

## Step1:
Open the terminal in the directory where you want to download/clone the project. Run
``` 
git clone https://github.com/inaveenchahar/shortsummary.git
```

# GUIDE TO USE THE PROJECT

## Step1: Setting up the virtual environment 
(create a virtual environment named 'env')
```
python3 -m venv env
```
(activate the environment)
```  
source env/bin/activate  
```
## Step2: Change into project directory 
``` 
cd shortsummary
```

## Step3: Set up the system requirements
``` 
pip install -r requirements.txt 
```

Note: If an error occurs during the installation of a pre-installed library then remove that particular library from requirements.txt and execute the command again to complete the remaining installations.

## Step4: Make Migrations
```
python3 manage.py makemigrations
python3 manage.py migrate
```

## Step5: Run server

```
python3 manage.py runserver
```


## Happy Reading
