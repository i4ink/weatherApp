from django.shortcuts import render, redirect
import os
from decouple import config

API_KEY = str(config('API_KEY'))

# Create your views here.
def home(request):
    import requests
    import json
    import pycountry

    # to find latitude and longitude - https://www.latlong.net/
    if request.method == 'POST':
        url = "https://air-quality.p.rapidapi.com/current/airquality"
        latitude = str(request.POST['latitude'])
        longitude = str(request.POST['longitude'])
        querystring = {"lat":latitude,"lon":longitude}

        headers = {
            'x-rapidapi-key': API_KEY,
            'x-rapidapi-host': "air-quality.p.rapidapi.com"
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        context = {}

        try:
            res = json.loads(response.content)
            # res = {'data': [{'mold_level': 0, 'aqi': 330, 'pm10': 5.36313, 'co': 695.109, 'o3': 87.9765, 'predominant_pollen_type': 'Molds', 'so2': 1.35787, 'pollen_level_tree': 0, 'pollen_level_weed': 0, 'no2': 3.75393, 'pm25': 4.14274, 'pollen_level_grass': 0}], 'city_name': 'Gumla', 'lon': 84.54, 'timezone': 'Asia/Kolkata', 'lat': 23.04, 'country_code': 'IN', 'state_code': '37'}
            # print('my result\n',res)

            value = int(res['data'][0]['aqi'])
            quality = ''
            desc = ''
            category_color = ''

            if value in range(0,51):
                quality = 'good'
                desc = 'Air quality is satisfactory, and air pollution poses little or no risk.'
                category_color = 'good'
            elif value in range(51,101):
                quality = 'moderate'
                desc = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
                category_color = 'moderate'
            elif value in range(101,151):
                quality = 'unhealthy for sensitive group'
                desc = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
                category_color = 'usg'
            elif value in range(151,201):
                quality = 'unhealthy'
                desc = 'Some members of the general public may experience health effects, members of sensitive groups may experience more serious health effects.'
                category_color = 'unhealthy'
            elif value in range(201,301):
                quality = 'very unhealthy'
                desc = 'Health alert: The risk of health effects is increased for everyone.'
                category_color = 'veryunhealthy'
            else:
                quality = 'hazardous'
                desc = 'Health warning of emergency conditions: everyone is more likely to be affected.'
                category_color = 'hazardous'

            context['res'] = res
            context['quality'] = quality
            context['desc'] = desc
            context['category_color'] = category_color
            context['country'] =  pycountry.countries.get(alpha_2=(res['country_code'])).name
        except Exception as e:
            print('debug',e)
            res = 'error...'
            context['res'] = res

        # res = {"data":[{"mold_level":0,"aqi":71,"pm10":35.1583,"co":512.362,"o3":84.132,"predomi nant_pollen_type":"Molds","so2":2.85357,"pollen_level_tree":0,"pollen_level_weed": 0,"no2":0.453176,"pm25":21.6392,"pollen_level_grass":0}],"city_name":"Gumla","lon" :84.54,"timezone":"Asia\/Kolkata","lat":23.04,"country_code":"IN","state_code":"37 "}


        return render(request, "home.html", context)

        
    else:
        url = "https://air-quality.p.rapidapi.com/current/airquality"

        querystring = {"lat":"23.041100","lon":"84.544000"}

        headers = {
            'x-rapidapi-key': API_KEY,
            'x-rapidapi-host': "air-quality.p.rapidapi.com"
            }
        # response = requests.request("GET", url, headers=headers, params=querystring)
        context = {}

        try:
            # res = json.loads(response.content)
            res = {'data': [{'mold_level': 0, 'aqi': 41, 'pm10': 5.36313, 'co': 695.109, 'o3': 87.9765, 'predominant_pollen_type': 'Molds', 'so2': 1.35787, 'pollen_level_tree': 0, 'pollen_level_weed': 0, 'no2': 3.75393, 'pm25': 4.14274, 'pollen_level_grass': 0}], 'city_name': 'Gumla', 'lon': 84.54, 'timezone': 'Asia/Kolkata', 'lat': 23.04, 'country_code': 'IN', 'state_code': '37'}
            # print('my result\n',res)

            value = int(res['data'][0]['aqi'])
            quality = ''
            desc = ''
            category_color = ''

            if value in range(0,51):
                quality = 'good'
                desc = 'Air quality is satisfactory, and air pollution poses little or no risk.'
                category_color = 'good'
            elif value in range(51,101):
                quality = 'moderate'
                desc = 'Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
                category_color = 'moderate'
            elif value in range(101,151):
                quality = 'unhealthy for sensitive group'
                desc = 'Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
                category_color = 'usg'
            elif value in range(151,201):
                quality = 'unhealthy'
                desc = 'Some members of the general public may experience health effects, members of sensitive groups may experience more serious health effects.'
                category_color = 'unhealthy'
            elif value in range(201,301):
                quality = 'very unhealthy'
                desc = 'Health alert: The risk of health effects is increased for everyone.'
                category_color = 'veryunhealthy'
            else:
                quality = 'hazardous'
                desc = 'Health warning of emergency conditions: everyone is more likely to be affected.'
                category_color = 'hazardous'

            context['res'] = res
            context['quality'] = quality
            context['desc'] = desc
            context['category_color'] = category_color
            context['country'] =  pycountry.countries.get(alpha_2=(res['country_code'])).name
        except Exception as e:
            print('debug',e)
            res = 'error...'
            context['res'] = res

        # res = {"data":[{"mold_level":0,"aqi":71,"pm10":35.1583,"co":512.362,"o3":84.132,"predomi nant_pollen_type":"Molds","so2":2.85357,"pollen_level_tree":0,"pollen_level_weed": 0,"no2":0.453176,"pm25":21.6392,"pollen_level_grass":0}],"city_name":"Gumla","lon" :84.54,"timezone":"Asia\/Kolkata","lat":23.04,"country_code":"IN","state_code":"37 "}


        return render(request, "home.html", context)

def about(request):
    return render(request, "about.html", {})