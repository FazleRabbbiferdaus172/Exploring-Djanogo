from django import forms
from django.core.validators import MaxLengthValidator


def check_for_f(value):
    if not 'f' in value:
        raise forms.ValidationError('NO f in the name')


class FromName(forms.Form):
    name = forms.CharField(validators=[check_for_f])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(
        required=False, widget=forms.HiddenInput, validators=[MaxLengthValidator(0, "HI, BBBOOOTTTT!!!!")])
    '''
    def clean_botcatcher(self):
        botccatcher = self.cleaned_data['botcatcher']
        if len(botccatcher):
            raise forms.ValidationError("Hi BOT!!!")
        return botccatcher
    '''
