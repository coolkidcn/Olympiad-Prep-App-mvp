from django.shortcuts import render 
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    return render(request, "members/home.html")