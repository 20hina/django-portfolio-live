from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from bio.models import Profile
from skills.models import Skill
from projects.models import Project
from experience.models import Experience
from education.models import Education
from .forms import ContactForm


# ─── LOGIN VIEW ──────────────────────────────────────────────────
def login_view(request):
    # If already logged in go to portfolio
    if request.user.is_authenticated:
        return redirect('portfolio')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check username and password
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(
                request,
                f'Welcome back {user.first_name or user.username}!'
            )
            return redirect('portfolio')
        else:
            messages.error(
                request,
                '❌ Invalid username or password!'
            )

    return render(request, 'login.html')


# ─── LOGOUT VIEW ─────────────────────────────────────────────────
def logout_view(request):
    logout(request)
    messages.success(request, '✅ Logged out successfully!')
    return redirect('login')


# ─── PORTFOLIO VIEW ───────────────────────────────────────────────
@login_required(login_url='login')
def index(request):
    try:
        # Get profile of LOGGED IN USER only!
        profile     = Profile.objects.get(user=request.user)
        skills      = Skill.objects.filter(profile=profile)
        project_list = Project.objects.filter(profile=profile)
        experiences = Experience.objects.filter(profile=profile)
        educations  = Education.objects.filter(profile=profile)

    except Profile.DoesNotExist:
        # Profile not created yet for this user
        profile      = None
        skills       = []
        project_list = []
        experiences  = []
        educations   = []

    # Handle contact form
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                '✅ Message sent successfully!'
            )
            return redirect('portfolio')
        else:
            messages.error(
                request,
                '❌ Something went wrong!'
            )
    else:
        form = ContactForm()

    context = {
        'profile'    : profile,
        'skills'     : skills,
        'projects'   : project_list,
        'experiences': experiences,
        'educations' : educations,
        'form'       : form,
        'user'       : request.user,
    }
    return render(request, 'index.html', context)


# ─── 404 ERROR PAGE ──────────────────────────────────────────────
def error_404(request, exception):
    return render(request, '404.html', status=404)