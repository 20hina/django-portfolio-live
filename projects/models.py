from django.db import models


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
        ordering = ['order']