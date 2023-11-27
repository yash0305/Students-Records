from django.db import models

class StudentsData(models.Model):
  name = models.CharField(max_length=100)
  standard = models.IntegerField()
  rollNo = models.IntegerField()
  age = models.IntegerField() 