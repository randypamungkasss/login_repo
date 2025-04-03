from django.db import models
from core.models import BaseModel

# Create your models here.
class Todo(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title