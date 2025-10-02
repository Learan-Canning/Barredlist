from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Post


# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Barred List Home Page!")

