from django.db import models
from bio.models import Profile


class Project(models.Model):
    # Link project to a specific profile
    profile     = models.ForeignKey(
                    Profile,
                    on_delete=models.CASCADE,
                    related_name='projects',
                    null=True,
                    blank=True
                  )
    title       = models.CharField(max_length=200)
    description = models.TextField()
    image       = models.ImageField(
                    upload_to='projects/',
                    blank=True,
                    null=True
                  )
    tech_stack  = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)
    live_link   = models.URLField(blank=True)
    order       = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']