from django import forms
from .models import Subscriber

class SubscribersForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        exclude = [""]
