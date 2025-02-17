from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required  # Import the login_required decorator
from members.models import Document, Mindmap, Member

# Create your views here.

def index(request):
    return render(request, "home.html")



@login_required  # Protects the view; redirects to login if not logged in
def myuser_dashboard(request):
    if Member.objects.filter(authuser=request.user).exists():  
        member = Member.objects.filter(authuser = request.user)[0]
        context = {
        'documents': Document.objects.filter(creatorId = member.userId),
        'mindmaps': Mindmap.objects.filter(creatorId = member.userId),
        'username':member.username,
        'user':request.user,
        'member':member,
        'friends': Member.objects.filter(friends = member),
        }
        return render(request, 'members/myuser_dashboard.html', context)
    else:
        member = Member.objects.create(
        username=request.user.username,
        authuser= request.user,
        )
        context = {
            'username':member.username,
            }
        return render(request, 'members/myuser_dashboard.html', context)
    return HttpResponse("No Response")


@login_required  # Protects the view; redirects to login if not logged in
def user_dashboard(request, memberName):
    if Member.objects.filter(username = memberName).exists():  
        member = Member.objects.filter(username = memberName)[0]
        context = {
        'documents': Document.objects.filter(creatorId = member.userId),
        'mindmaps': Mindmap.objects.filter(creatorId = member.userId),
        'username':member.username,
        'user':request.user,
        'member':member,
        'friends': Member.objects.filter(friends = member),
        }
        return render(request, 'members/user_dashboard.html', context)
    return HttpResponse("Not an User")
  

from .forms import DocumentForm  # Import your form

def add_Document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST) #, request.FILES if you have file uploads
        if form.is_valid():
            document = form.save(commit=False) # Don't save yet
            document.creatorId = request.user.id # Set the creator ID from the request
            document.save() # Now save
            return redirect('myuser_dashboard')  # Replace 'success_url'
    else:
        form = DocumentForm()

    return render(request, 'members/add_Document.html', {'form': form})