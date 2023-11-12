##############################################################
## Sommaire 
## la Doc :  https://flask.palletsprojects.com/en/2.2.x/

## Flask-tutorial : https://www.geeksforgeeks.org/flask-tutorial/#set
##############################################################

####################################################
## 1.  Installation de Flask 
####################################################

# activer l'environnement virtuel
$ mkdir flask-tutorial
$ cd flask-tutorial
$ python -m venv env 
$ env\Scripts\activate

# install flask 
$ pip install Flask

####################################################
## 2.  Project Layout
####################################################

# flask starter app 
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'


# structure of the final project 
flask_tutorial/ - le répertoire racine de notre projet

    .gitignore  
    
    config.py      - represente le fichier qui contient l'ensemble 
    
    run|Server|flaskblog.py      - c'est le point d'entrée de notre projet 
    
    requirements.txt - une liste des packages requis
    
    fbapp/ - le répertoire contenant les fichiers de notre application
    
        static/ - ce sont des fihiers fixes qui ne sont pas générés

        templates/ - les fichiers de templates HTML

        tests/ - le repertoire contient tous nos fichiers de test
        
        __init__.py  - le fichier permet de modularisé "fbapp"
        
        views.py     - le fichier de routage il gere les routes entrantes

#lancer le server flask
>set FLASK_APP=flaskblog.py (server file) 
>flask run or python flaskblog.py

####################################################
## 3.  static files 
####################################################

#To generate URLs for static files, use the special 'static' endpoint name:

url_for('static', filename='style.css')

#The file has to be stored on the filesystem as static/style.css.

####################################################
## 4.  Forms , Fields , validation and templates  
####################################################

############# Install Flask-WTF and WTForms

#Creating Forms and templating forms
FlaskWTF to create forms :https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/#creating-forms

#validate_on_submit() will check if it is a POST request and if it is valid.

#forms field and  validators 
WTforms doc : https://wtforms.readthedocs.io/en/3.0.x/


#######################################################
## .5 Models and Database  
#######################################################

# La Documentation Flask-SQLAlchemy : https://flask-sqlalchemy.palletsprojects.com/en/2.x/


############1.installer le SGBD sqlite 
C:\SQLlite\sqlite-tools-win32-x86-3360000>  sqlite3

############5.  Flask shell 
$ set FLASK_APP=run.py
$ flask shell
#ou
>>>python 
 
############2.installer l'ORM  pour flask 
$ pip install -U Flask-SQLAlchemy 

############3. creer les models.py pour chaque table et configurer l'URI pour la base de données 


#############3.creer un fichier de base de données ()

$ set FLASK_APP=run.py
$ flask shell


# effectuer des operations sur le shell flask
>>> from ourapplication import db
>>> db.create_all()  #initialise les models en base de données 
>>>import ourapplication # notre ourapplication peut etre un module ou alors un package 
>>> from ourapplication import app 
>>> app.config   #nos données de app.config
<Config {'DEBUG': False, 'TESTING': False, ...}
>>> from ourapplication import Content  # Content est un model et db est un objet sqlalchemy 
>>> db.session.add(Content("What's your favorite scary movie?", 0)) #permet d'ajouter un item à la base. En paramètres, vous passez l'instance de l'objet
>>> db.session.commit()     # similaire a commit de git , il permet de confirmer les modifications de nos requetes
>>> Content.query.all()     #renvoie tous les items de la table Content.
>>> [<fbapp.models.Content object at 0x1040518d0>]
>>> content = Content.query.get(1)  #renvoie l'itemsavec id=1.
<fbapp.models.Content object at 0x1061d98d0>
>>> content.description
"What's your favorite scary movie?"
>>> content.description = "Il s'appelle Juste Leblanc."
>>> db.session.rollback() #permet d'annuler les transactions non encore commités 
>>> content = Content.query.get(1)
<fbapp.models.Content object at 0x1061d98d0>
>>> db.session.delete(content)      # supprime le content qui est dans la variable "content"
>>> db.session.commit()

#######################################################
## 6. Large application as packages  
#######################################################

# Documentation : https://flask.palletsprojects.com/en/2.2.x/patterns/packages/?highlight=package

# project structure as a package not a module 
/yourapplication
    /yourapplication
        __init__.py     # this file turns /yourapplication folder into a package. it also create the app , configure app.config() and the db 
        /static
            style.css
        /templates
            layout.html
            index.html
            login.html
            ...
        models.py
        routes.py
        forms.py
    run.py          # this file import app from yourapplication and launch app.run()
            

#######################################################
## 7. User authentification with bcrypt and login
#######################################################

#####################Documentation flask-bcrypt :  https://flask-bcrypt.readthedocs.io/en/1.0.1/


#install flask-bcrypt
 pip install flask-bcrypt

#To use the extension simply import the class wrapper and pass the Flask app
bcrypt = Bcrypt(app)

#useful functions 
pw_hash = bcrypt.generate_password_hash('hunter2')..decode('utf-8')
bcrypt.check_password_hash(pw_hash, 'hunter2')


#####################Documentation flask-login : https://flask-login.readthedocs.io/en/latest/

#Flask-Login provides user session management for Flask.
# It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time.

#install flask-login
$ pip install flask-login



# provide a user_loader function in routes.py
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
    

#we have to addd UserMixin to bind the login_user with the model
class User(db.Model, UserMixin):
    ...
#useful fonction for routes.py
from flask_login import login_user, current_user, logout_user, login_required

#once a user is authenticated we can add this in the router before redirection to remember authenticated user
    login_user(user, remember=form.remember.data)
    

#in current_user we have the User Model instance for the authenticated user   
current_user

#check if the current user is authenticated
current_user.is_authenticated

#remove the credentials for the current_user
logout_user()


# login_required requires an authenticated user to acces this route 
@app.route("/account")
@login_required
def account():
    ...

#this following specifies that the view when a login route is blocked otherwise unauthrized error will be trigger
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

#######################################################
## 8.Images Processing with PIL for user_image 
#######################################################

#install Pillow to be able to import Image from PIL 
pip install Pillow

#import secrets secrets to be able to generate hexadecimal numbers

#import os to be able to manage filesystem path easily




#######################################################
## 9.CRUD Operations on a Model
#######################################################
