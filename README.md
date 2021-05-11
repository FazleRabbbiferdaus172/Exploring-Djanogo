# Learning-Django
This repo contains the django things I learned. Projects in this are the result of practice and exploration while learning django.


# Things to remember
1. Basic: Creating Project and app 
    1. **django-admin startproject ProjectName** to create a project
    2. **python manage.py startapp appName** to create a app and add the app in settings.py
    3. create urls.py in app folder and link this appname.urls.py to projectname.urls.py
2. Creating Static and template folder:
    1. static and template folder in root folder and let settings.py know this exists
    2. add {% load staticfiles %} after doctype in html file
    3. to link css use src = "{% static "css/style.css" %}" **nest css folder under static folder**  
3. Creating models:
    1. classes you create in models.py act as tables in database
    2. **python manage.py makemigrations appName** after creating classes in models.py
    3. **python manage.py migrate** after makemigrations
4. Django Admin:
    1. in admin.py import classes from models and register them in order to use them in website admin. **admin.site.register(className)** to register the table
    2. **python manage.py createsuperuser** . super user is need to access the admin.
5. Creating forms:
    1. In order to create a form first create a file forms.py inside the appName folder, then create a class that inherits forms.Form, create a form just like a model
    2. create a view for the class pass the form (dictinoary) as context.
    3. {{ form }} can be used to create the html
    4. {% csrf_token %} is a must to use the submit button
    5. In order to accept the token first check request.method is 'POST' or not if post then "form = forms.FormName( request.POST ) **POST MUST BE WRITTEN IN CAPITAL** then check if the form.is_valid() then you can do whatever you want with that. **YOU CAN USE CLEAN_DATA after validation**. As an example see the **views.py** file inside **formLearnAPP** folder of **LearnFromsProject** folder inside **Django level Three** folder or [Click Here](https://github.com/FazleRabbbiferdaus172/Exploring-Djanogo/blob/main/Django%20level%20three/LearnFormsProject/formLearnApp/views.py)
6. Forms validators:
    1. "from django.core import validators" to use validators in forms. See the official documentation.
    2. For coustome validation, make a function outsite of class and the class should thake **value** as the parameter then if the condition is false then use **raise forms.validationError("Your error message")** then you can use this function just like other validators from the django.core.validators . See the **Check_for_f** function from **forms.py** file of **formLearnAPP** folder inside of **LearnFromsProject** inside **Django level Three** folder or [Click Here](https://github.com/FazleRabbbiferdaus172/Exploring-Djanogo/blob/main/Django%20level%20three/LearnFormsProject/formLearnApp/forms.py)
    3. In order to use one finction to check all validation, create a method of formClass and name of the function should be **clean**. Then to access all data at once use **super().clean()** then you can have your valodations. [Click Here](https://github.com/FazleRabbbiferdaus172/Exploring-Djanogo/blob/main/Django%20level%20three/LearnFormsProject/formLearnApp/forms.py) to see an example.
7. ModelForms:
    1. import class inside the forms.py then create a class and inherit **forms.ModelForm**.
    2. write **Class Meta: model = models.modelname** to connect the forms with the model. **M in Meta is in capital** and **do not write models instead of model**.
    3. Inside meta class you can use **fields = "\_\_all\_\_"** if you want to use all model fields as form fields. you can also use exclude and indlude instead of fields.
    4. To save the data inside views.py check request.method and write **form = forms.FormName** **(Remember formName not modelName)** then check if the form **is_valid()** then.
    5. **form.save()** to save the form data to the model. 
    6. [Click Here](https://github.com/FazleRabbbiferdaus172/Exploring-Djanogo/tree/main/Django%20level%20three/ExerciseModelForms) to see an example.
8. Templates: Relative URLS, Template inheritance, Filters and Custome filters 
    1. For relative url inside templates inside appname/urls.py create a **app_name** variable and store the app name inside it.
    2. To use relative urls write **{% url 'appName:name' %}** **Do not leave any space after name or before appname inside the ''** and **name is the name you pass in the url do not forget to pass the name in side url**.
    3. For template inheritence use {% block block_name %} {% endblock %} in parent html and inside child html write {% extends 'filepath/fileName.html' %} then {% block block_name %} whatever you want to create {% endblock %}.
    4. To use filter write  **{ value|filterName:"args"}**.
    5. To use custome filtes, create a directory named **templatestags** inside **AppName** directory, inside **templatestags** directory create a **__init__.py** file, create another file **AppName_filters.py** .
    6. Inside **AppName_filters.py** write **from django import templates** and **register = template.Library()** and **@register.filter(name='nameYouWant')** then write the function.
    7. Write **{% load AppName_filters %}**. inside the html file in which you want to use the filter. **Don't load it inside parent html file(base.html) it won't work**.
    8. [Click Here](https://github.com/FazleRabbbiferdaus172/Exploring-Djanogo/tree/main/Django%20level%20Four/TemplateLearnProject) to see an example.

9. User registration and login:
    1. Inside the settings.py register the password hashers. See the document.
    2. Also set the password validators. **Make sure inside the INSTALLED_APPS  'django.contrib.auth','django.contrib.contenttypes' are registered**.
    3. Do not create a User table instead use the **User table of admin**. In order to use it first **from django.contrib.auth.models import User**.
    4. create a model class and first write **user = models.OneToOneField(User)** in order to use the User from the admin.
    5. Then you can create any field of your choice. **Do not forget to makemigrate and migrate after creating the models**. [Click Here](https://github.com/FazleRabbbiferdaus172/Exploring-Djanogo/blob/main/Django%20level%20Five/Basic_Project/basic_app/models.py) to see an example.
    6. Quick note if you want to have a inmage field you need to create a media directory inside project directory like you create templates, and static then inside setting.py write  **MEDIA_ROOT = MEDIA_DIR** and **MEDIA_URL = '/media/'**. [Click Here](https://github.com/FazleRabbbiferdaus172/Exploring-Djanogo/blob/main/Django%20level%20Five/Basic_Project/Basic_Project/settings.py) to see an example.
    7. In order to create the forms. first write **from django.contrib.auth.models import User** then import the models. Then create a modelForm for user model and any other model you create to take input from the user.
    8. [Click Here](https://github.com/FazleRabbbiferdaus172/Exploring-Djanogo/blob/main/Django%20level%20Five/Basic_Project/basic_app/forms.py) to see an example of user model form.
    9. Create form templates. [Click Here](https://github.com/FazleRabbbiferdaus172/Exploring-Djanogo/blob/main/Django%20level%20Five/Basic_Project/templates/basic_app/registration.html) to see an example of form template.
    10. In the views in order to set the password you should write **user.set_password(user.password)**. If you have image or csv or anytype of file as a form field you should check if the user has uploaded the file by using **if 'profile_pic' in request.FILES**. [Click Here](https://github.com/FazleRabbbiferdaus172/Exploring-Djanogo/blob/main/Django%20level%20Five/Basic_Project/basic_app/views.py) to see an example of view.py.
    11. For creating a login you should import **from django.contrib.auth import authenticate, login, logout
    from django.core.urlresolvers import reverse
    from django.contrib.auth.decorators import login_required**
    12. check if the user is authenticate and active by using **user = authenticate(username=username, password=password) and  user.is_active**
    13. use **login(request, user)** and return a render to login the user
    14. [Click Here](https://github.com/FazleRabbbiferdaus172/Exploring-Djanogo/blob/main/Django%20level%20Five/Basic_Project/basic_app/views.py) to see an example of view.py.

