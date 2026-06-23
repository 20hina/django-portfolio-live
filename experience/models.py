from django.db import models


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