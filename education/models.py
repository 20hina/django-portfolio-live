from django.db import models
from bio.models import Profile


class Education(models.Model):
    # Link education to a specific profile
    profile     = models.ForeignKey(
                    Profile,
                    on_delete=models.CASCADE,
                    related_name='educations',
                    null=True,
                    blank=True
                  )
    degree      = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year        = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order       = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    class Meta:
        ordering = ['order']