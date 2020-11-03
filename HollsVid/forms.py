from django import forms
from .models import video


class VideoFrom(forms.ModelForm):
    class Meta:
        model = video
        fields = ['url']
        labels = {'url':'Youtube URl'}


class SearchForm(forms.Form):
    search_tram = forms.CharField(max_length=100, label='search for  videos')
