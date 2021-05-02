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
12. In order to create a form first create a file forms.py inside the appName folder, then create a class that inherits forms.Form, create a form just like a model
13. create a view for the class pass the form (dictinoary) as context.
12. {{ form }} can be used to create the html
14. {% csrf_token %} is a must to use the submit button
15. In order to accept the token first check request.method is 'POST' or not if post then "form = forms.FormName( request.POST ) **POST MUST BE WRITTEN IN CAPITAL** then check if the form.is_valid() then you can do whatever you want with that. **YOU CAN USE CLEAN_DATA after validation**. As an example see the **views.py** of **formLEarnAPP** of **LearnFromsProject** inside **Django level Three** folder or [Click Here](https://github.com/FazleRabbbiferdaus172/Exploring-Djanogo/blob/main/Django%20level%20three/LearnFormsProject/formLearnApp/views.py)