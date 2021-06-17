from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Document, User, UserManager
import re
import bcrypt

def index(request):
    return render(request, 'signup.html')

def enter(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    errors = User.objects.reg_validator(request.POST)
    if errors:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/')

    hashed_pw = bcrypt.hashpw(
        request.POST['password'].encode(), bcrypt.gensalt()).decode()

    new_user = User.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST
        ['last_name'], email=request.POST['email'], password=hashed_pw
    )

    request.session['user_id'] = new_user.id
    return redirect('/success/')

    

def success(request):
    print("############# success route")
    if 'user_id' not in request.session:
        print("success but no user_id")
        return redirect('/')
    this_user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': this_user
    }
    print("success and something is weird")
    return render(request, 'success.html', context)


def login(request):
    print("####### login route")
    user = User.objects.filter(email=request.POST['email'])
    if user:
        existing_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), existing_user.password.encode()):
            request.session['user_id'] = existing_user.id
            return redirect('/success/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/enter/')
    messages.error(request, 'That Email is not in our system, please register for an account')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def edit(request): 
    print("####### edit route")
    if request.method == 'POST':
        newdoc = Document(
            docfile=request.FILES['docfile'],
        )
        newdoc.save()
        return HttpResponseRedirect('/edit/')
    context = {
        'documents': Document.objects.all()
    }
    print("success and something is weird")
    return render(request, 'edit.html', context)
