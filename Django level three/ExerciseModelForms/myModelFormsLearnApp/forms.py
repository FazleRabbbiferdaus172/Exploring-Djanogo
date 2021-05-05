from django import forms
from myModelFormsLearnApp.models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = "__all__"
