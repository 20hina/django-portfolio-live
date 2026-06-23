from django.shortcuts import render, redirect
from django.contrib import messages
from bio.models import Profile
from skills.models import Skill
from projects.models import Project
from experience.models import Experience
from education.models import Education
from .forms import ContactForm


def index(request):
    try:
        profile      = Profile.objects.first()
        skills       = Skill.objects.all()
        project_list = Project.objects.all()
        experiences  = Experience.objects.all()
        educations   = Education.objects.all()
    except Exception as e:
        profile      = None
        skills       = []
        project_list = []
        experiences  = []
        educations   = []

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                '✅ Message sent! I will get back to you soon.'
            )
            return redirect('/#contact')
        else:
            messages.error(
                request,
                '❌ Something went wrong. Please check your inputs.'
            )
    else:
        form = ContactForm()

    success = request.GET.get('success')

    context = {
        'profile'    : profile,
        'skills'     : skills,
        'projects'   : project_list,
        'experiences': experiences,
        'educations' : educations,
        'form'       : form,
        'success'    : success,
    }
    return render(request, 'index.html', context)


def error_404(request, exception):
    return render(request, '404.html', status=404)