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
    2. write **Class Meta: model = model.modelname** to connect the forms with the model **M in Meta is in capital** **do not write models instead of model**.
    3. Inside meta class you can use **fields = "__all__"** if you want to use all model fields as form fields. you can also use exclude and indlude instead of fields.
    4. To save the data inside views.py check request.method and write **form = forms.FormName** **(Remember formName not modelName)** then check if the form **is_valid()** then.
    5. **form.save()** to save the form data to the model. 