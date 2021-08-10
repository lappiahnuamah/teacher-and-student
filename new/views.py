from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Team, Review, Courses
from django.core.mail import send_mail
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegisterForm




# Create your views here.
def index(request):
    return render(request, 'index.html', )

@login_required(login_url='signin')
def about(request):
    context = {}
    return render(request, 'about.html', context)




@login_required(login_url='signin')
def pricing(request):
    context = {}
    return render(request, 'pricing.html', context)


@login_required(login_url='signin')
def team(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, 'team.html', context)


@login_required(login_url='signin')
def reviews(request):
    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, 'reviews.html', context)
    

@login_required(login_url='signin')
def courses(request):
    courses = Courses.objects.all()
    context = {'courses': courses}
    return render(request, 'courses.html', context)



def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')
        return render(request, 'signin.html',)


def signup(request):
    if request.user.is_authenticated:
            return redirect('/')
    else:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for "+ user)
                return redirect("signin")
        else:
            form = RegisterForm()
    return render(request, 'signup.html',{'form': form})


@login_required(login_url='signin')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        comment = request.POST.get('comment')

        data = {
            'name': name,
            'email':email,
            'subject':subject,
            'comment':comment
        }
        message = '''
        New message: {}

        From: {}
        '''.format(data['comment'], data['email'])
        send_mail(data['subject'], message, '', ['sandratb2121@gmail.com'])

    return render(request, 'contact.html',{})


def logoutUser(request):
    logout(request)
    return redirect('/')


def new_course(request):
    
    return render(request, 'new_course.html', {})
