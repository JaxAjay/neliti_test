from django import forms

class WeatherForm(forms.Form):
    latitude = forms.FloatField(required=True)
    longitude = forms.FloatField(required=True)