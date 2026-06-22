from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Project, Experience, Education
from .forms import ContactForm


def index(request):
    # ─── GET DATA FROM DATABASE ──────────────────────────────
    profile     = Profile.objects.first()
    skills      = Skill.objects.all()
    projects    = Project.objects.all()
    experiences = Experience.objects.all()
    educations  = Education.objects.all()

    # ─── HANDLE CONTACT FORM ─────────────────────────────────
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                '✅ Message sent successfully! I will get back to you soon.')
            return redirect('/#contact')
        else:
            messages.error(request,
                '❌ Something went wrong. Please check your inputs.')
    else:
        form = ContactForm()

    # ─── SUCCESS FLAG ─────────────────────────────────────────
    success = request.GET.get('success')

    context = {
        'profile'    : profile,
        'skills'     : skills,
        'projects'   : projects,
        'experiences': experiences,
        'educations' : educations,
        'form'       : form,
        'success'    : success,
    }
    return render(request, 'index.html', context)

# ─── 404 ERROR PAGE ──────────────────────────────────────────────
def error_404(request, exception):
    return render(request, '404.html', status=404)