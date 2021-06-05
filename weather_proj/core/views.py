from django.http.response import HttpResponse
from django.shortcuts import render , HttpResponse
import requests
from django.conf import settings
from .forms import WeatherForm
# Create your views here.

def get_weather(request):
    form = WeatherForm()
    error = ""
    output = {}
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            latitude = data['latitude']
            longitude = data['longitude']
            url = settings.WEATHER_URL
            url += "weatherapi/locationforecast/2.0/compact?lat=%s&lon=%s"%(latitude,longitude)
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;"}
            response = requests.get(url,headers=headers)
            if response.status_code == 200:
                output = response.json()
            else:
                error = response.text
    return render(request=request,template_name="core/weather.html", context= {'form':form ,
                                                                     'error':error , "output":output})