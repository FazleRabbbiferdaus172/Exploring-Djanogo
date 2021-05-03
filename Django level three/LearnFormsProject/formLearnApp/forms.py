from django import forms
from django.core.validators import MaxLengthValidator


# custome validator
def check_for_f(value):
    if not 'f' in value:
        raise forms.ValidationError('NO f in the name')


class FromName(forms.Form):
    name = forms.CharField(validators=[check_for_f])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    '''botcatcher = forms.CharField(
        required=False, widget=forms.HiddenInput, validators=[MaxLengthValidator(0, "HI, BBBOOOTTTT!!!!")])

    # without using the djnago.core.validators
    def clean_botcatcher(self):
        botccatcher = self.cleaned_data['botcatcher']
        if len(botccatcher):
            raise forms.ValidationError("Hi BOT!!!")
        return botccatcher
    '''

    def clean(self):

        all_cleaned_data = super().clean()

        if all_cleaned_data['email'] != all_cleaned_data['verify_email']:
            raise forms.ValidationError("Emails doesn't match")
