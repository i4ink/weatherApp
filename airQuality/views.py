from django.shortcuts import render, redirect

# Create your views here.
def home(requests):
    return render(requests, "home.html", {})

def about(requests):
    return render(requests, "about.html", {})