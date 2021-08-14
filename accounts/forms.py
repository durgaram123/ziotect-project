from django import forms
from django.db.models.base import Model
from django .forms import ModelForm
from .models import *

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'

class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields='__all__'

class TestimonialForm(forms.ModelForm):
    class Meta:
        model=Testimonial
        fields='__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model=Details
        fields='__all__'


