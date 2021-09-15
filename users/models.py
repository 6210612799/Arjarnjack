from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
# Create your models here.

class Couses(models.Model):
    subject = models.CharField(max_length=64)
    term = models.IntegerField()
    couseid = models.IntegerField()
    num_student = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.id} :subject {self.subject} term {self.term} Couses ID {self.couseid} student {self.num_student} year {self.year}"

class Nisit(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    couses = models.ManyToManyField(Couses, blank=True , related_name="student")
    def __str__(self):
        return f"{self.first}  {self.last}"