from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    extra_field = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "extra_field", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.extra_field = self.cleaned_data["extra_field"]
        if commit:
            user.save()
        return user