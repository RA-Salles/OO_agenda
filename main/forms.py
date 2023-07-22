from django.forms import ModelForm
from .models import Event, User

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

