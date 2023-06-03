from django.forms import ModelForm
from .models import Room, User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"  # all will create the exact form with all the components mentioned in the model
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'email']
