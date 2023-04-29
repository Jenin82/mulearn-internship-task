from django.db import models


# Create your models here.

class Todo(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)
  completion_date = models.CharField(null=True, blank=True, max_length=200)
  status = models.CharField(max_length=50, null=True, blank=True)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True) 
  
  class Meta:
    ordering = ['-updated', '-created']

  def __str__(self):
    return self.title