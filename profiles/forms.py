from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    birthday = forms.DateField(
        help_text='Required',
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
    )

    class Meta:
        model = User
        fields = ('username', 'birthday', 'password1', 'password2',)


class UpdateUserForm(forms.ModelForm):

    birthday = forms.DateField(
        help_text='Required',
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
    )

    class Meta:
        model = User
        fields = ('birthday', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        # try:
        self.fields['birthday'].initial = self.instance.profile.birthday
        # except:
        #     pass
