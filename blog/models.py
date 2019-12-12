from django.utils import timezone

from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "blog"
