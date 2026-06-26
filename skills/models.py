from django.db import models
from bio.models import Profile


class Skill(models.Model):
    profile    = models.ForeignKey(
                   Profile,
                   on_delete=models.CASCADE,
                   related_name='skills',
                   null=True,
                   blank=True
                 )
    name       = models.CharField(max_length=100)
    percentage = models.IntegerField(default=0)
    icon       = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-percentage']