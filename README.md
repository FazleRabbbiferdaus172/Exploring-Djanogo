# Learning-Django
This repo contains the django things I learned. Projects in this are the result of practice and exploration while learning django.


# Things to remember 
1. **django-admin startproject ProjectName** to create a project
2. **python manage.py startapp appName** to create a app and add the app in settings.py
3. create urls.py in app folder and link this appname.urls.py to projectname.urls.py
4. static and template folder in root folder and let settings.py know this exists
5. add {% load staticfiles %} after doctype in html file
6. to link css use src = "{% static "css/style.css" %}" **nest css folder under static folder**  
7. classes you create in models.py act as tables in database
8. **python manage.py makemigrations appName** after creating classes in models.py
9. **python manage.py migrate** after makemigrations
10. in admin.py import classes from models and register them in order to use them in website admin. **admin.site.register(className)** to register the table
11. **python manage.py createsuperuser** . super user is need to access the admin.