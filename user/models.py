from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
  host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  title = models.CharField(max_length=200)
  isCompleted = models.BooleanField(default=False)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True) 
  
  class Meta:
    ordering = ['-updated', '-created']
  
  def __str__(self):
    return self.title