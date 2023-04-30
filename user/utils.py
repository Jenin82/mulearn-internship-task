from enum import IntEnum

class TodoStatus(IntEnum):
  INPROGRESS = 1
  COMPLETED = 2
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]