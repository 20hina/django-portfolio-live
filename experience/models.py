from django.db import models
from bio.models import Profile


class Experience(models.Model):
    # Link experience to a specific profile
    profile     = models.ForeignKey(
                    Profile,
                    on_delete=models.CASCADE,
                    related_name='experiences',
                    null=True,
                    blank=True
                  )
    role        = models.CharField(max_length=200)
    company     = models.CharField(max_length=200)
    duration    = models.CharField(max_length=100)
    description = models.TextField()
    order       = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.role} @ {self.company}"

    class Meta:
        ordering = ['order']