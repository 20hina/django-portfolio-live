from django.db import models


class Profile(models.Model):
    name        = models.CharField(max_length=100)
    tagline     = models.CharField(max_length=200)
    about       = models.TextField()
    profile_img = models.ImageField(upload_to='profile/')
    cv          = models.FileField(
                    upload_to='cv/',
                    blank=True
                  )
    email       = models.EmailField()
    phone       = models.CharField(max_length=20, blank=True)
    location    = models.CharField(max_length=100, blank=True)
    github      = models.URLField(blank=True)
    linkedin    = models.URLField(blank=True)

    def __str__(self):
        return self.name