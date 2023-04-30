from django.db import models
from django.contrib.auth.models import User
from .utils import TodoStatus

# Create your models here.

class Todo(models.Model):
  host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  title = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)
  completion_date = models.DateField(null=True, blank=True, default=None)
  status = models.CharField(choices=TodoStatus.choices(), default=TodoStatus.PR, max_length=50)
  task_time = models.CharField(null=True, blank=True, default="under", max_length=50)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True) 
  
  class Meta:
    ordering = ['-updated', '-created']
    
  def is_task_time(self):
    import datetime
    if (datetime.date.today() > self.completion_date):
      self.task_time = "over"
    else:
      self.task_time = "under"
            
  def save(self, *args, **kwargs):
    self.is_task_time()
    super(Todo, self).save(*args, **kwargs)
  
  def __str__(self):
    return self.title