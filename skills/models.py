from django.db import models


class Skill(models.Model):
    name       = models.CharField(max_length=100)
    percentage = models.IntegerField(default=0)
    icon       = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-percentage']