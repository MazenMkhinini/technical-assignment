from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    def __str__(self): 
        return self.first_name + " " + self.last_name 

class TimeSlot(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    def __str__(self):
      return self.start

class TimeSlotOccupation(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.DO_NOTHING)
    timeslot = models.ForeignKey('TimeSlot', on_delete=models.DO_NOTHING)