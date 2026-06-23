from django.db import models


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