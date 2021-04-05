from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.db.models import fields
from app1.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('portfolio_site', 'profile_pic')


# def get_value_z(value):
#     if value[0] != 'z':
#         raise forms.ValidationError('Error asdd')

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    email1 = forms.EmailField(label='enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        emailq = all_clean_data['email']
        vmail = all_clean_data['email1']
        if vmail != emailq:
            raise forms.ValidationError({'email1': 'email not matching'})
        # def clean_botcatcher(self):
        #     botcatcher=self.cleaned_data['botcatcher']
        #     if len(botcatcher) > 0:
        #         raise forms.ValidationError('gotcha you bot')
        #     return botcatcher
