from enum import Enum

class TodoStatus(Enum):
  PR = 'In-Progress'
  CO = 'Completed'
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]