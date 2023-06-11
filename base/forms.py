from django.forms import ModelForm
from .models import Room, User
from django.contrib.auth.forms import (
    UserCreationForm,
)  # used to set 2 or more search parameter in one check

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"  # all will create the exact form with all the components mentioned in the model
        exclude = ["host", "participants"]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["avatar", "name", "username", "email", "bio"]
