from django.conf import settings
from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="projects",
        # on_delete=models.CASCADE, wasn't specified in instructions but seems like a good idea 6/17 16:38
    )

    def __str__(self):
        return self.name
