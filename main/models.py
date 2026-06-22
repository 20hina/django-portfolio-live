from django.db import models


# ─── PROFILE MODEL ───────────────────────────────────────────────
class Profile(models.Model):
    name        = models.CharField(max_length=100)
    tagline     = models.CharField(max_length=200)
    about       = models.TextField()
    profile_img = models.ImageField(upload_to='profile/')
    cv          = models.FileField(upload_to='cv/', blank=True)
    email       = models.EmailField()
    phone       = models.CharField(max_length=20, blank=True)
    location    = models.CharField(max_length=100, blank=True)
    github      = models.URLField(blank=True)
    linkedin    = models.URLField(blank=True)

    def __str__(self):
        return self.name


# ─── SKILL MODEL ─────────────────────────────────────────────────
class Skill(models.Model):
    name       = models.CharField(max_length=100)
    percentage = models.IntegerField(default=0)
    icon       = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-percentage']   # highest skill shown first


# ─── PROJECT MODEL ───────────────────────────────────────────────
class Project(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    image       = models.ImageField(upload_to='projects/')
    tech_stack  = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)
    live_link   = models.URLField(blank=True)
    order       = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']         # show in custom order


# ─── EXPERIENCE MODEL ────────────────────────────────────────────
class Experience(models.Model):
    role        = models.CharField(max_length=200)
    company     = models.CharField(max_length=200)
    duration    = models.CharField(max_length=100)
    description = models.TextField()
    order       = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.role} @ {self.company}"

    class Meta:
        ordering = ['order']


# ─── EDUCATION MODEL ─────────────────────────────────────────────
class Education(models.Model):
    degree      = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year        = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order       = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    class Meta:
        ordering = ['order']


# ─── CONTACT MODEL ───────────────────────────────────────────────
class Contact(models.Model):
    name     = models.CharField(max_length=100)
    email    = models.EmailField()
    subject  = models.CharField(max_length=200)
    message  = models.TextField()
    sent_at  = models.DateTimeField(auto_now_add=True)
    is_read  = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    class Meta:
        ordering = ['-sent_at']      # newest message shown first